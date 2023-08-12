tests/ui/test-attrs/test-should-fail-good-message.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind
// compile-flags: --test
#[test]
#[should_panic(expected = "foo")]
pub fn test_foo() {
    panic!("foo bar")
}

#[test]
#[should_panic(expected = "foo")]
pub fn test_foo_dynamic() {
    panic!("{} bar", "foo")
}


