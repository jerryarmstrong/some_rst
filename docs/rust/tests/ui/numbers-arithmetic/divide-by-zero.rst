tests/ui/numbers-arithmetic/divide-by-zero.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:attempt to divide by zero
// ignore-emscripten no processes

#[allow(unconditional_panic)]
fn main() {
    let y = 0;
    let _z = 1 / y;
}


