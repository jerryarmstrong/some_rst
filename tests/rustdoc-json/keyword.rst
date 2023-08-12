tests/rustdoc-json/keyword.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/98002>.

// Keywords should not be generated in rustdoc JSON output and this test
// ensures it.

#![feature(rustdoc_internals)]
#![no_std]

// @!has "$.index[*][?(@.name=='match')]"
// @has "$.index[*][?(@.name=='foo')]"

#[doc(keyword = "match")]
/// this is a test!
pub mod foo {}

// @!has "$.index[*][?(@.name=='hello')]"
// @!has "$.index[*][?(@.name=='bar')]"
#[doc(keyword = "hello")]
/// hello
mod bar {}


