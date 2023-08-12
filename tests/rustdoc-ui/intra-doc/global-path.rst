tests/rustdoc-ui/intra-doc/global-path.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Doc link path with empty prefix that resolves to "extern prelude" instead of a module.

// check-pass
// edition:2018

/// [::Unresolved]
//~^ WARN unresolved link to `::Unresolved`
pub struct Item;


