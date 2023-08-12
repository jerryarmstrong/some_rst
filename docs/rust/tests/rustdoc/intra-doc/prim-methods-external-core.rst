tests/rustdoc/intra-doc/prim-methods-external-core.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:my-core.rs
// build-aux-docs
// ignore-cross-compile
// only-linux

#![deny(rustdoc::broken_intra_doc_links)]
#![feature(no_core, lang_items)]
#![no_core]
#![crate_type = "rlib"]

// @has prim_methods_external_core/index.html
// @has - '//*[@id="main-content"]//a[@href="../my_core/primitive.char.html"]' 'char'
// @has - '//*[@id="main-content"]//a[@href="../my_core/primitive.char.html#method.len_utf8"]' 'char::len_utf8'

//! A [`char`] and its [`char::len_utf8`].

extern crate my_core;


