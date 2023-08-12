tests/rustdoc/auxiliary/external-cross.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deny(missing_docs)]
#[doc = include_str!("external-cross-doc.md")]
pub struct NeedMoreDocs;


