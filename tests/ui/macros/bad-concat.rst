tests/ui/macros/bad-concat.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: u32 = 42;
    let y: f64 = 3.14;
    let z = "foo";
    let _ = concat!(x, y, z, "bar");
    //~^ ERROR expected a literal
    //~| NOTE only literals
}


