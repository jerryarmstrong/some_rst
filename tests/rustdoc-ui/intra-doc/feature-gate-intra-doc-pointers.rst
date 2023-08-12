tests/rustdoc-ui/intra-doc/feature-gate-intra-doc-pointers.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! [pointer::add]
//~^ ERROR: experimental
//! [pointer::wrapping_add]
//~^ ERROR: experimental
//! [pointer] // This is explicitly allowed
//! [reference] // This is explicitly allowed


