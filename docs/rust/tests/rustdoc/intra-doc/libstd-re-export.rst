tests/rustdoc/intra-doc/libstd-re-export.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]
#![feature(intra_doc_pointers)]

pub use std::*;


