tests/ui/const-generics/generic_const_exprs/division.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

fn with_bound<const N: usize>() where [u8; N / 2]: Sized {
    let _: [u8; N / 2] = [0; N / 2];
}

fn main() {
    with_bound::<4>();
}


