tests/ui/array-slice-vec/vec-mut-iter-borrow.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut xs: Vec<isize> = vec![];

    for x in &mut xs {
        xs.push(1) //~ ERROR cannot borrow `xs`
    }
}


