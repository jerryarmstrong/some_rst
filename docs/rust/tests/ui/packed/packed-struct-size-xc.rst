tests/ui/packed/packed-struct-size-xc.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:packed.rs


extern crate packed;

use std::mem;

macro_rules! check {
    ($t:ty, $align:expr, $size:expr) => ({
        assert_eq!(mem::align_of::<$t>(), $align);
        assert_eq!(mem::size_of::<$t>(), $size);
    });
}

pub fn main() {
    check!(packed::P1S5, 1, 5);
    check!(packed::P2S6, 2, 6);
    check!(packed::P2CS8, 2, 8);
}


