tests/ui/occurs-check.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {

    let f;

    f = Box::new(f);
    //~^ ERROR mismatched types
    //~| cyclic type of infinite size
}


