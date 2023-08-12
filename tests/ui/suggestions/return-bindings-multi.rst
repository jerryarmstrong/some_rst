tests/ui/suggestions/return-bindings-multi.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a(i: i32) -> i32 {
    //~^ ERROR mismatched types
    let j = 2i32;
}

fn b(i: i32, j: i32) -> i32 {}
//~^ ERROR mismatched types

fn main() {}


