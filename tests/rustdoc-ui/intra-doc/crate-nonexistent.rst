tests/rustdoc-ui/intra-doc/crate-nonexistent.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

/// [crate::DoesNotExist]
//~^ ERROR unresolved link to `crate::DoesNotExist`
pub struct Item;


