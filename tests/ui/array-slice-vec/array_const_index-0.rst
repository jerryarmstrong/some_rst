tests/ui/array-slice-vec/array_const_index-0.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const A: &'static [i32] = &[];
const B: i32 = (&A)[1];
//~^ index out of bounds: the length is 0 but the index is 1
//~| ERROR evaluation of constant value failed

fn main() {
    let _ = B;
}


