tests/rustdoc-ui/intra-doc/private-from-crate-level.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

//! [my_module]
//~^ WARN public documentation for `private_from_crate_level` links to private item `my_module`

mod my_module {}


