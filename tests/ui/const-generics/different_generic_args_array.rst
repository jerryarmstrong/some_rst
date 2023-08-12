tests/ui/const-generics/different_generic_args_array.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that different const types are different.
#![feature(adt_const_params)]
#![allow(incomplete_features)]

struct Const<const V: [usize; 1]> {}

fn main() {
    let mut x = Const::<{ [3] }> {};
    x = Const::<{ [4] }> {};
    //~^ ERROR mismatched types
}


