src/tools/miri/tests/fail/intrinsics/ctlz_nonzero.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

mod rusti {
    extern "rust-intrinsic" {
        pub fn ctlz_nonzero<T>(x: T) -> T;
    }
}

pub fn main() {
    unsafe {
        use crate::rusti::*;

        ctlz_nonzero(0u8); //~ ERROR: `ctlz_nonzero` called on 0
    }
}


