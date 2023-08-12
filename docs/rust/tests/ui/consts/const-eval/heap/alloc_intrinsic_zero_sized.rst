tests/ui/consts/const-eval/heap/alloc_intrinsic_zero_sized.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(core_intrinsics)]
#![feature(const_heap)]
#![feature(inline_const)]

use std::intrinsics;

struct ZST;

fn main() {
    const {
        unsafe {
            let _ = intrinsics::const_allocate(0, 0) as *mut ZST;
        }
    }
}


