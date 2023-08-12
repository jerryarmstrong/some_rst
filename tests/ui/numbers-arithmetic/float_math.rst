tests/ui/numbers-arithmetic/float_math.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(core_intrinsics)]

use std::intrinsics::{fadd_fast, fsub_fast, fmul_fast, fdiv_fast, frem_fast};

#[inline(never)]
pub fn test_operations(a: f64, b: f64) {
    // make sure they all map to the correct operation
    unsafe {
        assert_eq!(fadd_fast(a, b), a + b);
        assert_eq!(fsub_fast(a, b), a - b);
        assert_eq!(fmul_fast(a, b), a * b);
        assert_eq!(fdiv_fast(a, b), a / b);
        assert_eq!(frem_fast(a, b), a % b);
    }
}

fn main() {
    test_operations(1., 2.);
    test_operations(10., 5.);
}


