tests/ui/numbers-arithmetic/overflowing-add.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:thread 'main' panicked at 'attempt to add with overflow'
// compile-flags: -C debug-assertions
// ignore-emscripten no processes

#![allow(arithmetic_overflow)]

fn main() {
    let _x = 200u8 + 200u8 + 200u8;
}


