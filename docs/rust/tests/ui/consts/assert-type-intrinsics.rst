tests/ui/consts/assert-type-intrinsics.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
#![feature(const_assert_type2)]
#![feature(core_intrinsics)]

use std::intrinsics;

#[allow(invalid_value)]
fn main() {
    use std::mem::MaybeUninit;

    const _BAD1: () = unsafe {
        MaybeUninit::<!>::uninit().assume_init();
        //~^ERROR: evaluation of constant value failed
    };
    const _BAD2: () = {
        intrinsics::assert_mem_uninitialized_valid::<&'static i32>();
        //~^ERROR: evaluation of constant value failed
    };
    const _BAD3: () = {
        intrinsics::assert_zero_valid::<&'static i32>();
        //~^ERROR: evaluation of constant value failed
    };
}


