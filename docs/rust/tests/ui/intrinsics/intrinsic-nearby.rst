tests/ui/intrinsics/intrinsic-nearby.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(core_intrinsics)]

use std::intrinsics::*;

fn main() {
    unsafe {
        assert_eq!(nearbyintf32(5.234f32), 5f32);
        assert_eq!(nearbyintf64(6.777f64), 7f64);
    }
}


