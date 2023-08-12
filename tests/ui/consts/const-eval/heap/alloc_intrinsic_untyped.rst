tests/ui/consts/const-eval/heap/alloc_intrinsic_untyped.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
#![feature(const_heap)]
#![feature(const_mut_refs)]
use std::intrinsics;

const BAR: *mut i32 = unsafe { intrinsics::const_allocate(4, 4) as *mut i32};
//~^ error: untyped pointers are not allowed in constant

fn main() {}


