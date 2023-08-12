tests/ui/coercion/coercion-slice.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we forbid coercion from `[T; n]` to `&[T]`

fn main() {
    let _: &[i32] = [0];
    //~^ ERROR mismatched types
    //~| expected `&[i32]`, found array `[{integer}; 1]`
}


