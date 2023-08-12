tests/rustdoc-ui/intra-doc/alias-ice.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

pub type TypeAlias = usize;

/// [broken cross-reference](TypeAlias::hoge) //~ ERROR
pub fn some_public_item() {}


