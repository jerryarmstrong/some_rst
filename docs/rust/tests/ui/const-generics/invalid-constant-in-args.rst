tests/ui/const-generics/invalid-constant-in-args.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::Cell;

fn main() {
    let _: Cell<&str, "a"> = Cell::new("");
    //~^ ERROR this struct takes 1 generic argument but 2 generic arguments were supplied
}


