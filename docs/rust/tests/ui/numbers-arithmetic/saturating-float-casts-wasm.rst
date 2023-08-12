tests/ui/numbers-arithmetic/saturating-float-casts-wasm.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// only-wasm32
// compile-flags: -Zmir-opt-level=0 -C target-feature=+nontrapping-fptoint

#![feature(test, stmt_expr_attributes)]
#![deny(overflowing_literals)]

#[path = "saturating-float-casts-impl.rs"]
mod implementation;

pub fn main() {
    implementation::run();
}


