tests/rustdoc/issue-99734-multiple-foreigns-w-same-name.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:issue-99734-aux.rs
// build-aux-docs
// ignore-cross-compile

#![crate_name = "foo"]

#[macro_use]
extern crate issue_99734_aux;

pub use issue_99734_aux::*;

// @count foo/index.html '//a[@class="fn"][@title="foo::main fn"]' 1

extern "C" {
    pub fn main() -> std::ffi::c_int;
}


