tests/ui/macros/assert-macro-static.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:panicked at 'test-assert-static'
// ignore-emscripten no processes

fn main() {
    assert!(false, "test-assert-static");
}


