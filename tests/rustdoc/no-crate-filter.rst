tests/rustdoc/no-crate-filter.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// compile-flags: -Z unstable-options --disable-per-crate-search

// @!has 'foo/struct.Foo.html' '//*[id="crate-search"]' ''
pub struct Foo;


