tests/rustdoc/inline_cross/impl-inline-without-trait.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:impl-inline-without-trait.rs
// build-aux-docs
// ignore-cross-compile

#![crate_name = "foo"]

extern crate impl_inline_without_trait;

// @has 'foo/struct.MyStruct.html'
// @has - '//*[@id="method.my_trait_method"]' 'fn my_trait_method()'
// @has - '//div[@class="docblock"]' 'docs for my_trait_method'
pub use impl_inline_without_trait::MyStruct;


