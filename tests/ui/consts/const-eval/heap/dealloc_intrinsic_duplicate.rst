tests/ui/consts/const-eval/heap/dealloc_intrinsic_duplicate.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
#![feature(const_heap)]

use std::intrinsics;

const _X: () = unsafe {
    let ptr = intrinsics::const_allocate(4, 4);
    intrinsics::const_deallocate(ptr, 4, 4);
    intrinsics::const_deallocate(ptr, 4, 4);
    //~^ error: evaluation of constant value failed
};

fn main() {}


