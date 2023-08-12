tests/rustdoc-ui/intra-doc/broken-reexport.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:intra-doc-broken.rs
// check-pass

#![deny(rustdoc::broken_intra_doc_links)]

extern crate intra_doc_broken;

pub use intra_doc_broken::foo;


