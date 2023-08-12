tests/ui/fully-qualified-type/fully-qualified-type-name1.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we use fully-qualified type names in error messages.

fn main() {
    let x: //~ NOTE expected due to the type of this binding
        Option<usize>; //~ NOTE expected due to this type
    x = 5;
    //~^ ERROR mismatched types
    //~| NOTE expected enum `Option<usize>`
    //~| NOTE expected enum `Option`, found integer
}


