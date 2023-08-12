tests/ui/occurs-check-2.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {

    let f;
    let g;

    g = f;
    f = Box::new(g);
    //~^  ERROR mismatched types
    //~| cyclic type of infinite size
}


