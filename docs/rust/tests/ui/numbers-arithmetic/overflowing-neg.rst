tests/ui/numbers-arithmetic/overflowing-neg.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:thread 'main' panicked at 'attempt to negate with overflow'
// ignore-emscripten no processes
// compile-flags: -C debug-assertions

#![allow(arithmetic_overflow)]

fn main() {
    let _x = -i8::MIN;
}


