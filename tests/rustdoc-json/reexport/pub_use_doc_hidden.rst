tests/rustdoc-json/reexport/pub_use_doc_hidden.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/106379>

#![feature(no_core)]
#![no_core]

mod repeat_n {
    #[doc(hidden)]
    pub struct RepeatN {}
}

pub use repeat_n::RepeatN;

// @count "$.index[*][?(@.name=='pub_use_doc_hidden')].inner.items[*]" 0
// @!has "$.index[*][?(@.kind=='struct')]"
// @!has "$.index[*][?(@.kind=='import')]"


