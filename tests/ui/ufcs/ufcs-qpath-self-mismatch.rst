tests/ui/ufcs/ufcs-qpath-self-mismatch.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::Add;

fn main() {
    <i32 as Add<u32>>::add(1, 2);
    //~^ ERROR cannot add `u32` to `i32`
    //~| ERROR cannot add `u32` to `i32`
    <i32 as Add<i32>>::add(1u32, 2);
    //~^ ERROR mismatched types
    <i32 as Add<i32>>::add(1, 2u32);
    //~^ ERROR mismatched types
}


