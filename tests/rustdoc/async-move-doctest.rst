tests/rustdoc/async-move-doctest.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test
// edition:2018

// Prior to setting the default edition for the doctest pre-parser,
// this doctest would fail due to a fatal parsing error.
// see https://github.com/rust-lang/rust/issues/59313

//! ```
//! fn foo() {
//!     drop(async move {});
//! }
//! ```


