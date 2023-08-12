tests/ui/suggestions/type-mismatch-struct-field-shorthand.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(dead_code)]

struct RGB { r: f64, g: f64, b: f64 }

fn main() {
    let (r, g, b): (f32, f32, f32) = (0., 0., 0.);
    let _ = RGB { r, g, b };
    //~^ ERROR mismatched types
    //~| ERROR mismatched types
    //~| ERROR mismatched types
}


