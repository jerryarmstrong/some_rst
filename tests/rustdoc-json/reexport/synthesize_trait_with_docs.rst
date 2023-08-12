tests/rustdoc-json/reexport/synthesize_trait_with_docs.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/105022>
// aux-build: trait_with_docs.rs

extern crate trait_with_docs;

pub struct Local;

impl trait_with_docs::HasDocs for Local {}

// @!has "$.index[*][?(@.name == 'HasDocs')]"


