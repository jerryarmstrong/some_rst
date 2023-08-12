tests/rustdoc/intra-doc/cross-crate/auxiliary/additional_doc.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "my_rand"]
#![deny(rustdoc::broken_intra_doc_links)]

pub trait RngCore {}
/// Rng extends [`RngCore`].
pub trait Rng: RngCore {}


