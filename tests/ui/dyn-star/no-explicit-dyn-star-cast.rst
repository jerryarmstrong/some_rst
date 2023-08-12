tests/ui/dyn-star/no-explicit-dyn-star-cast.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

fn make_dyn_star() {
    let i = 42usize;
    let dyn_i: dyn* Debug = i as dyn* Debug;
    //~^ ERROR casting `usize` as `dyn* Debug` is invalid
    //~| ERROR dyn* trait objects are unstable
    //~| ERROR dyn* trait objects are unstable
}

fn main() {
    make_dyn_star();
}


