tests/rustdoc/intra-doc/cross-crate/crate.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:intra-link-cross-crate-crate.rs
// build-aux-docs
#![crate_name = "outer"]
extern crate inner;
// @has outer/fn.f.html '//a[@href="../inner/fn.g.html"]' "crate::g"
pub use inner::f;


