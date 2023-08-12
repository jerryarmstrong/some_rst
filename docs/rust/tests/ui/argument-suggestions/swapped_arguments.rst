tests/ui/argument-suggestions/swapped_arguments.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X {}

fn two_args(_a: i32, _b: f32) {}
fn three_args(_a: i32, _b: f32, _c: &str) {}
fn four_args(_a: i32, _b: f32, _c: &str, _d: X) {}

fn main() {
  two_args(1.0, 1); //~ ERROR arguments to this function are incorrect
  three_args(1.0,   1,  ""); //~ ERROR arguments to this function are incorrect
  three_args(  1,  "", 1.0); //~ ERROR arguments to this function are incorrect
  three_args( "", 1.0,   1); //~ ERROR arguments to this function are incorrect

  four_args(1.0, 1, X {}, ""); //~ ERROR arguments to this function are incorrect
}


