tests/ui/numbers-arithmetic/overflowing-rsh-5.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// compile-flags: -C debug-assertions

#![deny(arithmetic_overflow)]

fn main() {
    let _n = 1i64 >> [64][0];
    //~^ ERROR: this arithmetic operation will overflow
}


