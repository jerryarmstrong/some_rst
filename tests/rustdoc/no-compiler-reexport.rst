tests/rustdoc/no-compiler-reexport.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unstable-options --document-hidden-items --document-private-items

#![crate_name = "foo"]

// @!has 'foo/index.html' '//code' 'extern crate std;'
// @!has 'foo/index.html' '//code' 'use std::prelude'
pub struct Foo;


