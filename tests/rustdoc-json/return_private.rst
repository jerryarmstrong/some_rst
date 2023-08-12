tests/rustdoc-json/return_private.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/96161>.
// ignore-tidy-linelength

#![feature(no_core)]
#![no_core]

mod secret {
    pub struct Secret;
}

// @is "$.index[*][?(@.name=='get_secret')].kind" \"function\"
// @is "$.index[*][?(@.name=='get_secret')].inner.decl.output.inner.name" \"secret::Secret\"
pub fn get_secret() -> secret::Secret {
    secret::Secret
}


