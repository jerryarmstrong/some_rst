tests/ui/fully-qualified-type/fully-qualified-type-name4.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we use fully-qualified type names in error messages.

use std::option::Option;

fn bar(x: usize) -> Option<usize> {
    return x;
    //~^ ERROR mismatched types
    //~| expected enum `Option<usize>`
    //~| found type `usize`
    //~| expected enum `Option`, found `usize`
}

fn main() {
}


