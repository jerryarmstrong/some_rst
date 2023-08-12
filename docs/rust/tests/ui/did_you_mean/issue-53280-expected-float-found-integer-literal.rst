tests/ui/did_you_mean/issue-53280-expected-float-found-integer-literal.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let sixteen: f32 = 16;
    //~^ ERROR mismatched types
    //~| HELP use a float literal
    let a_million_and_seventy: f64 = 1_000_070;
    //~^ ERROR mismatched types
    //~| HELP use a float literal
    let negative_nine: f32 = -9;
    //~^ ERROR mismatched types
    //~| HELP use a float literal


    // only base-10 literals get the suggestion

    let sixteen_again: f64 = 0x10;
    //~^ ERROR mismatched types
    let and_once_more: f32 = 0o20;
    //~^ ERROR mismatched types
}


