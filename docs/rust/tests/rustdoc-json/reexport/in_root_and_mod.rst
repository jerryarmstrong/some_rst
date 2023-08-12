tests/rustdoc-json/reexport/in_root_and_mod.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(no_core)]
#![no_core]

// @!has "$.index[*][?(@.name=='foo')]"
mod foo {
    // @has "$.index[*][?(@.name=='Foo')]"
    pub struct Foo;
}

// @has "$.index[*][?(@.kind=='import' && @.inner.source=='foo::Foo')]"
pub use foo::Foo;

pub mod bar {
    // @has "$.index[*][?(@.kind=='import' && @.inner.source=='crate::foo::Foo')]"
    pub use crate::foo::Foo;
}


