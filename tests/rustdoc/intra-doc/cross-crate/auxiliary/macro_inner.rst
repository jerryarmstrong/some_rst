tests/rustdoc/intra-doc/cross-crate/auxiliary/macro_inner.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "macro_inner"]
#![deny(rustdoc::broken_intra_doc_links)]

pub struct Foo;

/// See also [`Foo`]
#[macro_export]
macro_rules! my_macro {
    () => {}
}


