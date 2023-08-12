tests/ui/numeric/numeric-cast-2.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> i32 {
    4
}
fn main() {
    let x: u16 = foo();
    //~^ ERROR mismatched types
    let y: i64 = x + x;
    //~^ ERROR mismatched types
    let z: i32 = x + x;
    //~^ ERROR mismatched types
}


