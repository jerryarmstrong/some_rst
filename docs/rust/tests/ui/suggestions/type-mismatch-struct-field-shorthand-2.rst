tests/ui/suggestions/type-mismatch-struct-field-shorthand-2.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct RGB { r: f64, g: f64, b: f64 }

fn main() {
    let (r, g, c): (f32, f32, f32) = (0., 0., 0.);
    let _ = RGB { r, g, c };
    //~^ ERROR mismatched types
    //~| ERROR mismatched types
    //~| ERROR struct `RGB` has no field named `c`
}


