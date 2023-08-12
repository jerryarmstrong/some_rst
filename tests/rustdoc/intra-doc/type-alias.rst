tests/rustdoc/intra-doc/type-alias.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #86120.

#![deny(rustdoc::broken_intra_doc_links)]
#![crate_name = "foo"]

pub struct Foo;

/// You should really try [`Self::bar`]!
pub type Bar = Foo;

impl Bar {
    pub fn bar() {}
}

/// The minimum is [`Self::MIN`].
pub type Int = i32;

// @has foo/type.Bar.html '//a[@href="struct.Foo.html#method.bar"]' 'Self::bar'
// @has foo/type.Int.html '//a[@href="{{channel}}/std/primitive.i32.html#associatedconstant.MIN"]' 'Self::MIN'


