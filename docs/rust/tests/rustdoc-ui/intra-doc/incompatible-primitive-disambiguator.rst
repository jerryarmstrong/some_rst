tests/rustdoc-ui/intra-doc/incompatible-primitive-disambiguator.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]
//! [static@u8::MIN]
//~^ ERROR incompatible link kind


