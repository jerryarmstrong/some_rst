src/mem/mod.rs
==============

Last edited: 2023-03-09 18:36:25

Contents:

.. code-block:: rs

    // Trying to satisfy clippy here is hopeless
#![allow(clippy::style)]

#[allow(warnings)]
#[cfg(target_pointer_width = "16")]
type c_int = i16;
#[allow(warnings)]
#[cfg(not(target_pointer_width = "16"))]
type c_int = i32;

#[cfg(not(target_os = "solana"))]
use core::intrinsics::{atomic_load_unordered, atomic_store_unordered, exact_div};
#[cfg(not(target_os = "solana"))]
use core::mem;
#[cfg(not(target_os = "solana"))]
use core::ops::{BitOr, Shl};

// memcpy/memmove/memset have optimized implementations on some architectures
#[cfg(not(target_os = "solana"))]
#[cfg_attr(
    all(not(feature = "no-asm"), target_arch = "x86_64"),
    path = "x86_64.rs"
)]
mod impls;

#[cfg(not(target_os = "solana"))]
intrinsics! {
    #[mem_builtin]
    #[cfg_attr(not(all(target_os = "windows", target_env = "gnu")), linkage = "weak")]
    pub unsafe extern "C" fn memcpy(dest: *mut u8, src: *const u8, n: usize) -> *mut u8 {
        impls::copy_forward(dest, src, n);
        dest
    }

    #[mem_builtin]
    #[cfg_attr(not(all(target_os = "windows", target_env = "gnu")), linkage = "weak")]
    pub unsafe extern "C" fn memmove(dest: *mut u8, src: *const u8, n: usize) -> *mut u8 {
        let delta = (dest as usize).wrapping_sub(src as usize);
        if delta >= n {
            // We can copy forwards because either dest is far enough ahead of src,
            // or src is ahead of dest (and delta overflowed).
            impls::copy_forward(dest, src, n);
        } else {
            impls::copy_backward(dest, src, n);
        }
        dest
    }

    #[mem_builtin]
    #[cfg_attr(not(all(target_os = "windows", target_env = "gnu")), linkage = "weak")]
    pub unsafe extern "C" fn memset(s: *mut u8, c: crate::mem::c_int, n: usize) -> *mut u8 {
        impls::set_bytes(s, c as u8, n);
        s
    }

    #[mem_builtin]
    #[cfg_attr(not(all(target_os = "windows", target_env = "gnu")), linkage = "weak")]
    pub unsafe extern "C" fn memcmp(s1: *const u8, s2: *const u8, n: usize) -> i32 {
        impls::compare_bytes(s1, s2, n)
    }

    #[mem_builtin]
    #[cfg_attr(not(all(target_os = "windows", target_env = "gnu")), linkage = "weak")]
    pub unsafe extern "C" fn bcmp(s1: *const u8, s2: *const u8, n: usize) -> i32 {
        memcmp(s1, s2, n)
    }

    #[mem_builtin]
    #[cfg_attr(not(all(target_os = "windows", target_env = "gnu")), linkage = "weak")]
    pub unsafe extern "C" fn strlen(s: *const u8) -> usize {
        let mut n = 0;
        let mut s = s;
        while *s != 0 {
            n += 1;
            s = s.offset(1);
        }
        n
    }
}

// `bytes` must be a multiple of `mem::size_of::<T>()`
#[cfg(not(target_os = "solana"))]
#[cfg_attr(not(target_has_atomic_load_store = "8"), allow(dead_code))]
fn memcpy_element_unordered_atomic<T: Copy>(dest: *mut T, src: *const T, bytes: usize) {
    unsafe {
        let n = exact_div(bytes, mem::size_of::<T>());
        let mut i = 0;
        while i < n {
            atomic_store_unordered(dest.add(i), atomic_load_unordered(src.add(i)));
            i += 1;
        }
    }
}

// `bytes` must be a multiple of `mem::size_of::<T>()`
#[cfg(not(target_os = "solana"))]
#[cfg_attr(not(target_has_atomic_load_store = "8"), allow(dead_code))]
fn memmove_element_unordered_atomic<T: Copy>(dest: *mut T, src: *const T, bytes: usize) {
    unsafe {
        let n = exact_div(bytes, mem::size_of::<T>());
        if src < dest as *const T {
            // copy from end
            let mut i = n;
            while i != 0 {
                i -= 1;
                atomic_store_unordered(dest.add(i), atomic_load_unordered(src.add(i)));
            }
        } else {
            // copy from beginning
            let mut i = 0;
            while i < n {
                atomic_store_unordered(dest.add(i), atomic_load_unordered(src.add(i)));
                i += 1;
            }
        }
    }
}

// `T` must be a primitive integer type, and `bytes` must be a multiple of `mem::size_of::<T>()`
#[cfg(not(target_os = "solana"))]
#[cfg_attr(not(target_has_atomic_load_store = "8"), allow(dead_code))]
fn memset_element_unordered_atomic<T>(s: *mut T, c: u8, bytes: usize)
where
    T: Copy + From<u8> + Shl<u32, Output = T> + BitOr<T, Output = T>,
{
    unsafe {
        let n = exact_div(bytes, mem::size_of::<T>());

        // Construct a value of type `T` consisting of repeated `c`
        // bytes, to let us ensure we write each `T` atomically.
        let mut x = T::from(c);
        let mut i = 1;
        while i < mem::size_of::<T>() {
            x = x << 8 | T::from(c);
            i += 1;
        }

        // Write it to `s`
        let mut i = 0;
        while i < n {
            atomic_store_unordered(s.add(i), x);
            i += 1;
        }
    }
}

#[cfg(not(target_os = "solana"))]
intrinsics! {
    #[cfg(target_has_atomic_load_store = "8")]
    pub unsafe extern "C" fn __llvm_memcpy_element_unordered_atomic_1(dest: *mut u8, src: *const u8, bytes: usize) -> () {
        memcpy_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "16")]
    pub unsafe extern "C" fn __llvm_memcpy_element_unordered_atomic_2(dest: *mut u16, src: *const u16, bytes: usize) -> () {
        memcpy_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "32")]
    pub unsafe extern "C" fn __llvm_memcpy_element_unordered_atomic_4(dest: *mut u32, src: *const u32, bytes: usize) -> () {
        memcpy_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "64")]
    pub unsafe extern "C" fn __llvm_memcpy_element_unordered_atomic_8(dest: *mut u64, src: *const u64, bytes: usize) -> () {
        memcpy_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "128")]
    pub unsafe extern "C" fn __llvm_memcpy_element_unordered_atomic_16(dest: *mut u128, src: *const u128, bytes: usize) -> () {
        memcpy_element_unordered_atomic(dest, src, bytes);
    }

    #[cfg(target_has_atomic_load_store = "8")]
    pub unsafe extern "C" fn __llvm_memmove_element_unordered_atomic_1(dest: *mut u8, src: *const u8, bytes: usize) -> () {
        memmove_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "16")]
    pub unsafe extern "C" fn __llvm_memmove_element_unordered_atomic_2(dest: *mut u16, src: *const u16, bytes: usize) -> () {
        memmove_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "32")]
    pub unsafe extern "C" fn __llvm_memmove_element_unordered_atomic_4(dest: *mut u32, src: *const u32, bytes: usize) -> () {
        memmove_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "64")]
    pub unsafe extern "C" fn __llvm_memmove_element_unordered_atomic_8(dest: *mut u64, src: *const u64, bytes: usize) -> () {
        memmove_element_unordered_atomic(dest, src, bytes);
    }
    #[cfg(target_has_atomic_load_store = "128")]
    pub unsafe extern "C" fn __llvm_memmove_element_unordered_atomic_16(dest: *mut u128, src: *const u128, bytes: usize) -> () {
        memmove_element_unordered_atomic(dest, src, bytes);
    }

    #[cfg(target_has_atomic_load_store = "8")]
    pub unsafe extern "C" fn __llvm_memset_element_unordered_atomic_1(s: *mut u8, c: u8, bytes: usize) -> () {
        memset_element_unordered_atomic(s, c, bytes);
    }
    #[cfg(target_has_atomic_load_store = "16")]
    pub unsafe extern "C" fn __llvm_memset_element_unordered_atomic_2(s: *mut u16, c: u8, bytes: usize) -> () {
        memset_element_unordered_atomic(s, c, bytes);
    }
    #[cfg(target_has_atomic_load_store = "32")]
    pub unsafe extern "C" fn __llvm_memset_element_unordered_atomic_4(s: *mut u32, c: u8, bytes: usize) -> () {
        memset_element_unordered_atomic(s, c, bytes);
    }
    #[cfg(target_has_atomic_load_store = "64")]
    pub unsafe extern "C" fn __llvm_memset_element_unordered_atomic_8(s: *mut u64, c: u8, bytes: usize) -> () {
        memset_element_unordered_atomic(s, c, bytes);
    }
    #[cfg(target_has_atomic_load_store = "128")]
    pub unsafe extern "C" fn __llvm_memset_element_unordered_atomic_16(s: *mut u128, c: u8, bytes: usize) -> () {
        memset_element_unordered_atomic(s, c, bytes);
    }
}

// MEM functions have been rewritten to copy 8 byte chunks.  No
// compensation for alignment is made here with the requirement that
// the underlying hardware supports unaligned loads/stores.  If the
// number of store operations is greater than 8 the memory operation
// is performed in the run-time system instead, by calling the
// corresponding "C" function.

#[cfg(all(target_os = "solana", not(target_feature = "static-syscalls")))]
mod syscalls {
    extern "C" {
        pub fn sol_memcpy_(dest: *mut u8, src: *const u8, n: u64);
        pub fn sol_memmove_(dest: *mut u8, src: *const u8, n: u64);
        pub fn sol_memset_(s: *mut u8, c: u8, n: u64);
        pub fn sol_memcmp_(s1: *const u8, s2: *const u8, n: u64, result: *mut i32);
    }
}

#[cfg(all(target_os = "solana", target_feature = "static-syscalls"))]
mod syscalls {
    pub(crate) fn sol_memcpy_(dest: *mut u8, src: *const u8, n: u64) {
        let syscall: extern "C" fn(*mut u8, *const u8, u64) =
            unsafe { core::mem::transmute(1904002211u64) }; // murmur32 hash of "sol_memcpy_"
        syscall(dest, src, n)
    }

    pub(crate) fn sol_memmove_(dest: *mut u8, src: *const u8, n: u64) {
        let syscall: extern "C" fn(*mut u8, *const u8, u64) =
            unsafe { core::mem::transmute(1128493560u64) }; // murmur32 hash of "sol_memmove_"
        syscall(dest, src, n)
    }

    pub(crate) fn sol_memcmp_(dest: *const u8, src: *const u8, n: u64, result: *mut i32) {
        let syscall: extern "C" fn(*const u8, *const u8, u64, *mut i32) =
            unsafe { core::mem::transmute(1608310321u64) }; // murmur32 hash of "sol_memcmp_"
        syscall(dest, src, n, result)
    }

    pub(crate) fn sol_memset_(dest: *mut u8, c: u8, n: u64) {
        let syscall: extern "C" fn(*mut u8, u8, u64) =
            unsafe { core::mem::transmute(930151202u64) }; // murmur32 hash of "sol_memset_"
        syscall(dest, c, n)
    }
}

#[cfg(target_os = "solana")]
use self::syscalls::*;

#[cfg(target_os = "solana")]
const NSTORE_THRESHOLD: usize = 15;

#[cfg(target_os = "solana")]
#[cfg_attr(
    all(feature = "mem-unaligned", not(feature = "mangled-names")),
    no_mangle
)]
#[inline]
pub unsafe extern "C" fn memcpy(dest: *mut u8, src: *const u8, n: usize) -> *mut u8 {
    let chunks = (n / 8) as isize;
    let nstore = n - (7 * chunks) as usize;
    if nstore > NSTORE_THRESHOLD {
        sol_memcpy_(dest, src, n as u64);
        return dest;
    }
    let mut i: isize = 0;
    if chunks != 0 {
        let dest_64 = dest as *mut _ as *mut u64;
        let src_64 = src as *const _ as *const u64;
        while i < chunks {
            *dest_64.offset(i) = *src_64.offset(i);
            i += 1;
        }
        i *= 8;
    }
    while i < n as isize {
        *dest.offset(i) = *src.offset(i);
        i += 1;
    }
    dest
}

#[cfg(target_os = "solana")]
#[cfg_attr(
    all(feature = "mem-unaligned", not(feature = "mangled-names")),
    no_mangle
)]
#[inline]
pub unsafe extern "C" fn memmove(dest: *mut u8, src: *const u8, n: usize) -> *mut u8 {
    let chunks = (n / 8) as isize;
    let nstore = n - (7 * chunks) as usize;
    if nstore > NSTORE_THRESHOLD {
        sol_memmove_(dest, src, n as u64);
        return dest;
    }
    if src < dest as *const u8 {
        // copy from end
        let mut i = n as isize;
        while i > chunks * 8 {
            i -= 1;
            *dest.offset(i) = *src.offset(i);
        }
        i = chunks;
        if i > 0 {
            let dest_64 = dest as *mut _ as *mut u64;
            let src_64 = src as *const _ as *const u64;
            while i > 0 {
                i -= 1;
                *dest_64.offset(i) = *src_64.offset(i);
            }
        }
    } else {
        // copy from beginning
        let mut i: isize = 0;
        if chunks != 0 {
            let dest_64 = dest as *mut _ as *mut u64;
            let src_64 = src as *const _ as *const u64;
            while i < chunks {
                *dest_64.offset(i) = *src_64.offset(i);
                i += 1;
            }
            i *= 8;
        }
        while i < n as isize {
            *dest.offset(i) = *src.offset(i);
            i += 1;
        }
    }
    dest
}

#[cfg(target_os = "solana")]
#[cfg_attr(
    all(feature = "mem-unaligned", not(feature = "mangled-names")),
    no_mangle
)]
#[inline]
pub unsafe extern "C" fn memset(s: *mut u8, c: c_int, n: usize) -> *mut u8 {
    let chunks = (n / 8) as isize;
    let nstore = n - (7 * chunks) as usize;
    if nstore > NSTORE_THRESHOLD {
        sol_memset_(s, c as u8, n as u64);
        return s;
    }
    let mut i: isize = 0;
    if chunks != 0 {
        let mut c_64 = c as u64 & 0xFF as u64;
        c_64 |= c_64 << 8;
        c_64 |= c_64 << 16;
        c_64 |= c_64 << 32;
        let s_64 = s as *mut _ as *mut u64;
        while i < chunks {
            *s_64.offset(i) = c_64;
            i += 1;
        }
        i *= 8;
    }
    while i < n as isize {
        *s.offset(i) = c as u8;
        i += 1;
    }
    s
}

#[cfg(target_os = "solana")]
#[cfg_attr(
    all(feature = "mem-unaligned", not(feature = "mangled-names")),
    no_mangle
)]
#[inline]
pub unsafe extern "C" fn memcmp(s1: *const u8, s2: *const u8, n: usize) -> i32 {
    let chunks = (n / 8) as isize;
    let nstore = n - (7 * chunks) as usize;
    if nstore > NSTORE_THRESHOLD {
        let mut result = 0;
        sol_memcmp_(s1, s2, n as u64, &mut result as *mut i32);
        return result;
    }
    let mut i: isize = 0;
    if chunks != 0 {
        let s1_64 = s1 as *const _ as *const u64;
        let s2_64 = s2 as *const _ as *const u64;
        while i < chunks {
            let a = *s1_64.offset(i);
            let b = *s2_64.offset(i);
            if a != b {
                break;
            }
            i += 1;
        }
        i *= 8;
    }
    while i < n as isize {
        let a = *s1.offset(i);
        let b = *s2.offset(i);
        if a != b {
            return a as i32 - b as i32;
        }
        i += 1;
    }
    0
}


