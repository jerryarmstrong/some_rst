tests/ui/type/type-check/point-at-inference-3.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let mut v = Vec::new();
    v.push(0i32);
    v.push(0);
    v.push(1u32); //~ ERROR mismatched types
    //~^ NOTE expected `i32`, found `u32`
    //~| NOTE arguments to this method are incorrect
    //~| NOTE associated function defined here
    //~| HELP change the type of the numeric literal from `u32` to `i32`
}


