tests/ui/consts/const-eval/heap/dealloc_intrinsic_zero_sized.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(core_intrinsics)]
#![feature(const_heap)]
#![feature(inline_const)]

use std::intrinsics;

fn main() {
    const {
        unsafe {
            let ptr1 = intrinsics::const_allocate(0, 0);
            let ptr2 = intrinsics::const_allocate(0, 0);
            intrinsics::const_deallocate(ptr1, 0, 0);
            intrinsics::const_deallocate(ptr2, 0, 0);
        }
    }
}


