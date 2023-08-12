tests/rustdoc-json/type/extern.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

extern {
    /// No inner information
    pub type Foo;
}

// @is "$.index[*][?(@.docs=='No inner information')].name" '"Foo"'
// @is "$.index[*][?(@.docs=='No inner information')].kind" '"foreign_type"'
// @!has "$.index[*][?(@.docs=='No inner information')].inner"


