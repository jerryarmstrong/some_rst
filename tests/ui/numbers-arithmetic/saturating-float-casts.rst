tests/ui/numbers-arithmetic/saturating-float-casts.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-Zmir-opt-level=0

#![feature(test, stmt_expr_attributes)]
#![deny(overflowing_literals)]

#[path = "saturating-float-casts-impl.rs"]
mod implementation;

pub fn main() {
    implementation::run();
}


