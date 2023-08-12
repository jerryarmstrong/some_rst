src/tools/miri/tests/fail/intrinsics/cttz_nonzero.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

mod rusti {
    extern "rust-intrinsic" {
        pub fn cttz_nonzero<T>(x: T) -> T;
    }
}

pub fn main() {
    unsafe {
        use crate::rusti::*;

        cttz_nonzero(0u8); //~ ERROR: `cttz_nonzero` called on 0
    }
}


