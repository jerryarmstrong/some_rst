tests/ui/attributes/tool_attributes.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Scoped attributes should not trigger an unused attributes lint.

#![deny(unused_attributes)]

fn main() {
    #[rustfmt::skip]
    foo ();
}

fn foo() {
    assert!(true);
}


