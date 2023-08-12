tests/rustdoc/external-cross.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:external-cross.rs
// ignore-cross-compile

#![crate_name="host"]

extern crate external_cross;

// @has host/struct.NeedMoreDocs.html
// @has - '//h2' 'Cross-crate imported docs'
pub use external_cross::NeedMoreDocs;


