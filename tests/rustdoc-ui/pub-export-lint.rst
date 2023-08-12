tests/rustdoc-ui/pub-export-lint.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

/// [aloha]
//~^ ERROR unresolved link to `aloha`
pub use std::task::RawWakerVTable;


