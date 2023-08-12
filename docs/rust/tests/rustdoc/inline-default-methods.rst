tests/rustdoc/inline-default-methods.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:inline-default-methods.rs
// ignore-cross-compile

extern crate inline_default_methods;

// @has inline_default_methods/trait.Foo.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'fn bar(&self);'
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'fn foo(&mut self) { ... }'
pub use inline_default_methods::Foo;


