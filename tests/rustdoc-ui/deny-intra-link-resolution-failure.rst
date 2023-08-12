tests/rustdoc-ui/deny-intra-link-resolution-failure.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

/// [v2] //~ ERROR
pub fn foo() {}


