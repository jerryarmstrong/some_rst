tests/ui/panics/test-panic.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// check-stdout
// compile-flags: --test
// ignore-emscripten

#[test]
fn test_foo() {
    panic!()
}


