tests/ui/numbers-arithmetic/overflowing-pow-signed.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:thread 'main' panicked at 'attempt to multiply with overflow'
// ignore-emscripten no processes
// compile-flags: -C debug-assertions

fn main() {
    let _x = 2i32.pow(1024);
}


