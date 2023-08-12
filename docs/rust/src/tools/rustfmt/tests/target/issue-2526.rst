src/tools/rustfmt/tests/target/issue-2526.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that rustfmt will not warn about comments exceeding max width around lifetime.
// See #2526.

// comment comment comment comment comment comment comment comment comment comment comment comment comment
fn foo() -> F<'a> {
    bar()
}
// comment comment comment comment comment comment comment comment comment comment comment comment comment


