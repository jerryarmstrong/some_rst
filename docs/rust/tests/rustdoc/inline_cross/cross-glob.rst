tests/rustdoc/inline_cross/cross-glob.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:cross-glob.rs
// build-aux-docs
// ignore-cross-compile

extern crate inner;

// @has cross_glob/struct.SomeStruct.html
// @has cross_glob/fn.some_fn.html
// @!has cross_glob/enum.Shadowed.html
// @!has cross_glob/index.html '//code' 'pub use inner::*;'
#[doc(inline)]
pub use inner::*;

// This type shadows the glob-imported enum `Shadowed`.
// @has cross_glob/type.Shadowed.html
pub type Shadowed = u8;


