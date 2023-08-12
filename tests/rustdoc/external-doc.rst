tests/rustdoc/external-doc.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has external_doc/struct.IncludeStrDocs.html
// @has - '//h2' 'External Docs'
// @has - '//h3' 'Inline Docs'
#[doc = include_str!("auxiliary/external-doc.md")]
/// ## Inline Docs
pub struct IncludeStrDocs;

macro_rules! dir { () => { "auxiliary" } }

// @has external_doc/struct.EagerExpansion.html
// @has - '//h2' 'External Docs'
#[doc = include_str!(concat!(dir!(), "/external-doc.md"))]
/// ## Inline Docs
pub struct EagerExpansion;


