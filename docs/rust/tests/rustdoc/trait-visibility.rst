tests/rustdoc/trait-visibility.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:trait-visibility.rs

#![crate_name = "foo"]

extern crate trait_visibility;

// @has foo/trait.Bar.html '//a[@href="#tymethod.foo"]/..' "fn foo()"
pub use trait_visibility::Bar;


