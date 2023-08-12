src/tools/miri/tests/fail/intrinsics/rem-by-zero.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

use std::intrinsics::*;

fn main() {
    unsafe {
        let _n = unchecked_rem(3u32, 0); //~ ERROR: calculating the remainder with a divisor of zero
    }
}


