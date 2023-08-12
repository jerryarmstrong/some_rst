library/std/src/sys/sbf/alloc.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! This is an implementation of a global allocator on the SBF platform.
//! In that situation there's no actual runtime for us
//! to lean on for allocation, so instead we provide our own!
//!
//! The crate itself provides a global allocator which on SBF has no
//! synchronization as there are no threads!

use crate::alloc::{GlobalAlloc, Layout, System};

#[stable(feature = "alloc_system_type", since = "1.28.0")]
unsafe impl GlobalAlloc for System {
    #[inline]
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        sol_alloc_free_(layout.size() as u64, 0)
        // 0 as *mut u8
    }

    #[inline]
    unsafe fn alloc_zeroed(&self, layout: Layout) -> *mut u8 {
        sol_alloc_free_(layout.size() as u64, 0)
        // 0 as *mut u8
    }

    #[inline]
    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        sol_alloc_free_(layout.size() as u64, ptr as u64);
    }

    // #[inline]
    // unsafe fn realloc(&self, ptr: *mut u8, layout: Layout, new_size: usize) -> *mut u8 {
    //     sol_alloc_free_(layout.size() as u64, 0)
    //     // 0 as *mut u8
    // }
}

#[cfg(not(target_feature = "static-syscalls"))]
extern "C" {
    fn sol_alloc_free_(size: u64, ptr: u64) -> *mut u8;
}

#[cfg(target_feature = "static-syscalls")]
fn sol_alloc_free_(size: u64, ptr: u64) -> *mut u8 {
    let syscall: extern "C" fn(u64, u64) -> *mut u8 =
        unsafe { core::mem::transmute(2213547663u64) }; // murmur32 hash of "sol_alloc_free_"
    syscall(size, ptr)
}


