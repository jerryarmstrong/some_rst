tests/ui/array-slice-vec/vector-no-ann.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _foo = Vec::new();
    //~^ ERROR type annotations needed
}


