tests/rustdoc-json/enums/use_variant_foreign.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build: color.rs

extern crate color;

// @is "$.index[*][?(@.inner.name == 'Red')].kind" '"import"'
pub use color::Color::Red;

// @!has "$.index[*][?(@.name == 'Red')]"
// @!has "$.index[*][?(@.name == 'Color')]"


