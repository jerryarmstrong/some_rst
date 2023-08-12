tests/rustdoc/intra-doc/auxiliary/intra-link-reexport-additional-docs.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "inner"]

/// Links to [f()]
pub struct Inner;

pub fn f() {}


