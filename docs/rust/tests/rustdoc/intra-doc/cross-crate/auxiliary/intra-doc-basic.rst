tests/rustdoc/intra-doc/cross-crate/auxiliary/intra-doc-basic.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "a"]
#![deny(rustdoc::broken_intra_doc_links)]

pub struct Foo;

/// Link to [Foo]
pub struct Bar;


