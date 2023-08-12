tests/ui/array-slice-vec/slice-mut-2.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test mutability and slicing syntax.

fn main() {
    let x: &[isize] = &[1, 2, 3, 4, 5];
    // Can't mutably slice an immutable slice
    let slice: &mut [isize] = &mut [0, 1];
    let _ = &mut x[2..4]; //~ERROR cannot borrow `*x` as mutable, as it is behind a `&` reference
}


