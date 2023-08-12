tests/rustdoc/auto-impl-primitive.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustdoc_internals)]

#![crate_name = "foo"]

pub use std::fs::File;

// @has 'foo/primitive.i16.html' '//h2[@id="synthetic-implementations"]' 'Auto Trait Implementation'
#[doc(primitive = "i16")]
/// I love poneys!
mod prim {}


