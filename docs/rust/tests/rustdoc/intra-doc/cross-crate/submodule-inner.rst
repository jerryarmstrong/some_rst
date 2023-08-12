tests/rustdoc/intra-doc/cross-crate/submodule-inner.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:submodule-inner.rs
// build-aux-docs
#![deny(rustdoc::broken_intra_doc_links)]

extern crate a;

// @has 'submodule_inner/struct.Foo.html' '//a[@href="../a/bar/struct.Bar.html"]' 'Bar'
pub use a::foo::Foo;


