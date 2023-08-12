tests/rustdoc-ui/intra-doc/field-ice.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]
//~^NOTE the lint level is defined here

/// [`Foo::bar`]
/// [`Foo::bar()`]
//~^ERROR incompatible link kind for `Foo::bar`
//~|HELP to link to the field, remove the disambiguator
//~|NOTE this link resolved to a field, which is not a function
pub struct Foo {
    pub bar: u8
}


