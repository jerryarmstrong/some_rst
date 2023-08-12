tests/rustdoc/inline_cross/trait-vis.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:trait-vis.rs

extern crate inner;

// @has trait_vis/struct.SomeStruct.html
// @has - '//h3[@class="code-header"]' 'impl Clone for SomeStruct'
pub use inner::SomeStruct;


