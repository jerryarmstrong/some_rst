src/tools/clippy/tests/ui/trailing_zeros.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_parens)]
#![warn(clippy::verbose_bit_mask)]

fn main() {
    let x: i32 = 42;
    let _ = (x & 0b1111 == 0); // suggest trailing_zeros
    let _ = x & 0b1_1111 == 0; // suggest trailing_zeros
    let _ = x & 0b1_1010 == 0; // do not lint
    let _ = x & 1 == 0; // do not lint
}


