tests/ui/macros/assert-macro-owned.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:panicked at 'test-assert-owned'
// ignore-emscripten no processes

#![allow(non_fmt_panics)]

fn main() {
    assert!(false, "test-assert-owned".to_string());
}


