tests/rustdoc/nul-error.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-aux-docs
// ignore-cross-compile

#![crate_name = "foo"]

// @has foo/fn.foo.html '//code' ''
#[doc = "Attempted to pass a string containing `\0`"]
pub fn foo() {}


