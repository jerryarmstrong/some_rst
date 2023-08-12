tests/rustdoc/inline_cross/hidden-use.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:rustdoc-hidden.rs
// build-aux-docs
// ignore-cross-compile

extern crate rustdoc_hidden;

// @has hidden_use/index.html
// @!hasraw - 'rustdoc_hidden'
// @!hasraw - 'Bar'
// @!has hidden_use/struct.Bar.html
#[doc(hidden)]
pub use rustdoc_hidden::Bar;


