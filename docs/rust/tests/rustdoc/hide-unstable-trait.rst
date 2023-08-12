tests/rustdoc/hide-unstable-trait.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:unstable-trait.rs

#![crate_name = "foo"]
#![feature(private_trait)]

extern crate unstable_trait;

// @hasraw foo/struct.Foo.html 'bar'
// @hasraw foo/struct.Foo.html 'bar2'
#[doc(inline)]
pub use unstable_trait::Foo;


