tests/assembly/is_aligned.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // assembly-output: emit-asm
// min-llvm-version: 15.0
// only-x86_64
// revisions: opt-speed opt-size
// [opt-speed] compile-flags: -Copt-level=1
// [opt-size] compile-flags: -Copt-level=s
#![crate_type="rlib"]

#![feature(core_intrinsics)]
#![feature(pointer_is_aligned)]

// CHECK-LABEL: is_aligned_to_unchecked
// CHECK: decq
// CHECK-NEXT: testq
// CHECK-NEXT: sete
// CHECK: retq
#[no_mangle]
pub unsafe fn is_aligned_to_unchecked(ptr: *const u8, align: usize) -> bool {
    unsafe {
        std::intrinsics::assume(align.is_power_of_two())
    }
    ptr.is_aligned_to(align)
}

// CHECK-LABEL: is_aligned_1
// CHECK: movb $1
// CHECK: retq
#[no_mangle]
pub fn is_aligned_1(ptr: *const u8) -> bool {
    ptr.is_aligned()
}

// CHECK-LABEL: is_aligned_2
// CHECK: testb $1
// CHECK-NEXT: sete
// CHECK: retq
#[no_mangle]
pub fn is_aligned_2(ptr: *const u16) -> bool {
    ptr.is_aligned()
}

// CHECK-LABEL: is_aligned_4
// CHECK: testb $3
// CHECK-NEXT: sete
// CHECK: retq
#[no_mangle]
pub fn is_aligned_4(ptr: *const u32) -> bool {
    ptr.is_aligned()
}

// CHECK-LABEL: is_aligned_8
// CHECK: testb $7
// CHECK-NEXT: sete
// CHECK: retq
#[no_mangle]
pub fn is_aligned_8(ptr: *const u64) -> bool {
    ptr.is_aligned()
}


