tests/ui/consts/const-eval/heap/alloc_intrinsic_nontransient_fail.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
#![feature(const_heap)]
#![feature(const_mut_refs)]
use std::intrinsics;

const FOO: *const i32 = foo();
//~^ ERROR untyped pointers are not allowed in constant

const fn foo() -> &'static i32 {
    let t = unsafe {
        let i = intrinsics::const_allocate(4, 4) as * mut i32;
        *i = 20;
        i
    };
    unsafe { &*t }
}
fn main() {
}


