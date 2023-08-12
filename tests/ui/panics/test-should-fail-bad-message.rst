tests/ui/panics/test-should-fail-bad-message.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// check-stdout
// compile-flags: --test
// ignore-emscripten

#[test]
#[should_panic(expected = "foobar")]
fn test_foo() {
    panic!("blah")
}


