tests/rustdoc/intra-doc/prim-methods.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

// @has prim_methods/index.html
// @has - '//*[@id="main-content"]//a[@href="{{channel}}/std/primitive.char.html"]' 'char'
// @has - '//*[@id="main-content"]//a[@href="{{channel}}/std/primitive.char.html#method.len_utf8"]' 'char::len_utf8'

//! A [`char`] and its [`char::len_utf8`].


