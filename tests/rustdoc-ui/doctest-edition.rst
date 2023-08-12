tests/rustdoc-ui/doctest-edition.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![deny(rustdoc::invalid_rust_codeblocks)]
//~^ NOTE lint level is defined here

// By default, rustdoc should use the edition of the crate.
//! ```
//! foo'b'
//! ```
//~^^^ ERROR could not parse
//~| NOTE prefix `foo` is unknown

// Rustdoc should respect `edition2018` when highlighting syntax.
//! ```edition2018
//! foo'b'
//! ```


