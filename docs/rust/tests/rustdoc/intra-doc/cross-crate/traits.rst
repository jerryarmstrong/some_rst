tests/rustdoc/intra-doc/cross-crate/traits.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:traits.rs
// build-aux-docs
#![deny(rustdoc::broken_intra_doc_links)]

extern crate inner;
use inner::SomeTrait;

pub struct SomeStruct;

 // @has 'traits/struct.SomeStruct.html' '//a[@href="../inner/trait.SomeTrait.html"]' 'SomeTrait'
impl SomeTrait for SomeStruct {
    // @has 'traits/struct.SomeStruct.html' '//a[@href="../inner/trait.SomeTrait.html"]' 'a trait'
    fn foo() {}
}


