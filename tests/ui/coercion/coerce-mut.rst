tests/ui/coercion/coerce-mut.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(x: &mut i32) {}

fn main() {
    let x = 0;
    f(&x);
    //~^ ERROR mismatched types
    //~| expected mutable reference `&mut i32`
    //~| found reference `&{integer}`
    //~| types differ in mutability
}


