tests/ui/numbers-arithmetic/overflowing-rsh-2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// compile-flags: -C debug-assertions

#![deny(arithmetic_overflow)]

fn main() {
    let _x = -1_i32 >> -1;
    //~^ ERROR: this arithmetic operation will overflow
}


