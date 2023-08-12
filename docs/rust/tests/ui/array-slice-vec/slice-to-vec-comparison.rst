tests/ui/array-slice-vec/slice-to-vec-comparison.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = &[];
    let b: &Vec<u8> = &vec![];
    a > b;
    //~^ ERROR mismatched types
}


