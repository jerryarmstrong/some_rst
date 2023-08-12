src/tools/miri/tests/fail/intrinsics/div-by-zero.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

use std::intrinsics::*;

fn main() {
    unsafe {
        let _n = unchecked_div(1i64, 0); //~ERROR: dividing by zero
    }
}


