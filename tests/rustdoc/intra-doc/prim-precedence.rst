tests/rustdoc/intra-doc/prim-precedence.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

pub mod char {
    /// [char]
    // @has prim_precedence/char/struct.Inner.html '//a/@href' '{{channel}}/std/primitive.char.html'
    pub struct Inner;
}

/// See [prim@char]
// @has prim_precedence/struct.MyString.html '//a/@href' '{{channel}}/std/primitive.char.html'
pub struct MyString;

/// See also [crate::char] and [mod@char]
// @has prim_precedence/struct.MyString2.html '//*[@href="char/index.html"]' 'crate::char'
// @has - '//*[@href="char/index.html"]' 'mod@char'
pub struct MyString2;


