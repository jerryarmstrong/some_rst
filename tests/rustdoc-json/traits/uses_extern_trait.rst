tests/rustdoc-json/traits/uses_extern_trait.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
pub fn drop_default<T: core::default::Default>(_x: T) {}

// @!has "$.index[*][?(@.name=='Debug')]"
// @!has "$.index[*][?(@.name=='Default')]"


