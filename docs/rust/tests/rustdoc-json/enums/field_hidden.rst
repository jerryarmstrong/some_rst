tests/rustdoc-json/enums/field_hidden.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/100529>.

#![no_core]
#![feature(no_core)]

// @has "$.index[*][?(@.name=='ParseError')]"
// @has "$.index[*][?(@.name=='UnexpectedEndTag')]"
// @is "$.index[*][?(@.name=='UnexpectedEndTag')].inner.kind.tuple" [null]
// @is "$.index[*][?(@.name=='UnexpectedEndTag')].inner.discriminant" null

pub enum ParseError {
    UnexpectedEndTag(#[doc(hidden)] u32),
}


