tests/rustdoc-json/enums/doc_link_to_foreign_variant.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build: color.rs

//! The purpose of this test it to have a link to [a foreign variant](Red).

extern crate color;
use color::Color::Red;

// @set red = "$.index[*][?(@.inner.is_crate == true)].links.Red"

// @!has "$.index[*][?(@.name == 'Red')]"
// @!has "$.index[*][?(@.name == 'Color')]"


