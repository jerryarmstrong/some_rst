tests/ui/suggestions/bad-hex-float-lit.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _f: f32 = 0xAAf32;
    //~^ ERROR mismatched types
    //~| HELP rewrite this

    let _f: f32 = 0xAB_f32;
    //~^ ERROR mismatched types
    //~| HELP rewrite this

    let _f: f64 = 0xFF_f64;
    //~^ ERROR mismatched types
    //~| HELP rewrite this
}


