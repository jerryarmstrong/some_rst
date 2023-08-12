tests/ui/suggestions/dont-suggest-doc-hidden-variant-for-enum/hidden-parent.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:hidden-parent.rs

extern crate hidden_parent;

fn main() {
    let x: Option<i32> = 1i32; //~ ERROR mismatched types
}


