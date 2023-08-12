tests/rustdoc/inline_cross/inline_hidden.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:rustdoc-hidden.rs
// build-aux-docs
// ignore-cross-compile

extern crate rustdoc_hidden;

#[doc(no_inline)]
pub use rustdoc_hidden::Foo;

// @has inline_hidden/fn.foo.html
// @!has - '//a/@title' 'Foo'
pub fn foo(_: Foo) {}


