tests/ui/consts/const-eval/ub-int-array.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // stderr-per-bitwidth
//! Test the "array of int" fast path in validity checking, and in particular whether it
//! points at the right array element.

use std::mem;

#[repr(C)]
union MaybeUninit<T: Copy> {
    uninit: (),
    init: T,
}

const UNINIT_INT_0: [u32; 3] = unsafe {
    [
        MaybeUninit { uninit: () }.init,
        //~^ ERROR evaluation of constant value failed
        //~| uninitialized
        1,
        2,
    ]
};
const UNINIT_INT_1: [u32; 3] = unsafe {
    mem::transmute(
        [
            0u8,
            0u8,
            0u8,
            0u8,
            1u8,
            MaybeUninit { uninit: () }.init,
            //~^ ERROR evaluation of constant value failed
            //~| uninitialized
            1u8,
            1u8,
            2u8,
            2u8,
            MaybeUninit { uninit: () }.init,
            2u8,
        ]
    )
};
const UNINIT_INT_2: [u32; 3] = unsafe {
    mem::transmute(
        [
            0u8,
            0u8,
            0u8,
            0u8,
            1u8,
            1u8,
            1u8,
            1u8,
            2u8,
            2u8,
            2u8,
            MaybeUninit { uninit: () }.init,
            //~^ ERROR evaluation of constant value failed
            //~| uninitialized
        ]
    )
};

fn main() {}


