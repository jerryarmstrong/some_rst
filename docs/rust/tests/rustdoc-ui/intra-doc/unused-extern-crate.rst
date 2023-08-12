tests/rustdoc-ui/intra-doc/unused-extern-crate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --extern zip=whatever.rlib
#![deny(rustdoc::broken_intra_doc_links)]
/// See [zip] crate.
//~^ ERROR unresolved
pub struct ArrayZip;


