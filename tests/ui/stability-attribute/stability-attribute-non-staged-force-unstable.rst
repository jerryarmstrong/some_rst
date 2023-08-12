tests/ui/stability-attribute/stability-attribute-non-staged-force-unstable.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Zforce-unstable-if-unmarked

#[unstable()] //~ ERROR: stability attributes may not be used
#[stable()] //~ ERROR: stability attributes may not be used
fn main() {}


