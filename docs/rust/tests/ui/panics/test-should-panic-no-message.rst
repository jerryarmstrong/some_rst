tests/ui/panics/test-should-panic-no-message.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// compile-flags: --test
// check-stdout
// ignore-emscripten no processes

#[test]
#[should_panic(expected = "foo")]
pub fn test_explicit() {
    panic!()
}


