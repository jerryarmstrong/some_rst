tests/ui/lint/lint-type-overflow2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O

#![deny(overflowing_literals)]

fn main() {
    let x2: i8 = --128; //~ ERROR literal out of range for `i8`

    let x = -3.40282357e+38_f32; //~ ERROR literal out of range for `f32`
    let x =  3.40282357e+38_f32; //~ ERROR literal out of range for `f32`
    let x = -1.7976931348623159e+308_f64; //~ ERROR literal out of range for `f64`
    let x =  1.7976931348623159e+308_f64; //~ ERROR literal out of range for `f64`
}


