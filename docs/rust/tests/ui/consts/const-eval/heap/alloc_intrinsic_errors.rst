tests/ui/consts/const-eval/heap/alloc_intrinsic_errors.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
#![feature(const_heap)]
#![feature(const_mut_refs)]
use std::intrinsics;

const FOO: i32 = foo();
const fn foo() -> i32 {
    unsafe {
        let _ = intrinsics::const_allocate(4, 3) as *mut i32;
        //~^ error: evaluation of constant value failed
    }
    1
}

fn main() {}


