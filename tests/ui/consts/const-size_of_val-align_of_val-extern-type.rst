tests/ui/consts/const-size_of_val-align_of_val-extern-type.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]
#![feature(core_intrinsics)]
#![feature(const_size_of_val, const_align_of_val)]

use std::intrinsics::{min_align_of_val, size_of_val};

extern "C" {
    type Opaque;
}

const _SIZE: usize = unsafe { size_of_val(&4 as *const i32 as *const Opaque) }; //~ ERROR constant
const _ALIGN: usize = unsafe { min_align_of_val(&4 as *const i32 as *const Opaque) }; //~ ERROR constant

fn main() {}


