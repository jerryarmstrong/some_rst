tests/ui/suggestions/dont-suggest-doc-hidden-variant-for-enum/hidden-child.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:hidden-child.rs

// FIXME(compiler-errors): This currently suggests the wrong thing.
// UI test exists to track the problem.

extern crate hidden_child;

fn main() {
    let x: Option<i32> = 1i32; //~ ERROR mismatched types
}


