tests/rustdoc/redirect-map-empty.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unstable-options --generate-redirect-map

#![crate_name = "foo"]

// @!has foo/redirect-map.json
pub struct Foo;


