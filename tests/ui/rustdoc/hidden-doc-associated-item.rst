tests/ui/rustdoc/hidden-doc-associated-item.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// See issue #85526.
// This test should produce no warnings.

#![deny(missing_docs)]
//! Crate docs

#[doc(hidden)]
pub struct Foo;

impl Foo {
    pub fn bar() {}
}

fn main() {}


