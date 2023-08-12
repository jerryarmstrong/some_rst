tests/ui/array-slice-vec/array-not-vector.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _x: i32 = [1, 2, 3];
    //~^ ERROR mismatched types
    //~| expected `i32`, found array

    let x: &[i32] = &[1, 2, 3];
    let _y: &i32 = x;
    //~^ ERROR mismatched types
    //~| expected reference `&i32`
    //~| found reference `&[i32]`
    //~| expected `i32`, found slice
}


