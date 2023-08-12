tests/ui/borrowck/borrowck-for-loop-head-linkage.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::iter::repeat;

fn main() {
    let mut vector = vec![1, 2];
    for &x in &vector {
        let cap = vector.capacity();
        vector.extend(repeat(0));      //~ ERROR cannot borrow
        vector[1] = 5;   //~ ERROR cannot borrow
    }
}


