tests/rustdoc-json/primitives/primitive_overloading.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --document-private-items

// Regression test for <https://github.com/rust-lang/rust/issues/98006>.

#![feature(rustdoc_internals)]
#![feature(no_core)]

#![no_core]

// @has "$.index[*][?(@.name=='usize')]"
// @has "$.index[*][?(@.name=='prim')]"

#[doc(primitive = "usize")]
/// This is the built-in type `usize`.
mod prim {
}


