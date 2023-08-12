tests/ui/custom-attribute-multisegment.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Unresolved multi-segment attributes are not treated as custom.

mod existent {}

#[existent::nonexistent] //~ ERROR failed to resolve: could not find `nonexistent` in `existent`
fn main() {}


