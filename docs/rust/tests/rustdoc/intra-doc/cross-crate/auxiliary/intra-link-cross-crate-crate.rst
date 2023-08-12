tests/rustdoc/intra-doc/cross-crate/auxiliary/intra-link-cross-crate-crate.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "inner"]

/// Links to [crate::g]
pub fn f() {}
pub fn g() {}


