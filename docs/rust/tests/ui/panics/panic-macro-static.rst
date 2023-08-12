tests/ui/panics/panic-macro-static.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:panicked at 'test-fail-static'
// ignore-emscripten no processes

fn main() {
    panic!("test-fail-static");
}


