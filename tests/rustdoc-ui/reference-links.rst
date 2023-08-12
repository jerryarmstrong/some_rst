tests/rustdoc-ui/reference-links.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that errors point to the reference, not to the title text.
#![deny(rustdoc::broken_intra_doc_links)]
//! Links to [a] [link][a]
//!
//! [a]: std::process::Comman
//~^ ERROR unresolved


