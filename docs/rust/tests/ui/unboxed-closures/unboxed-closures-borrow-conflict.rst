tests/ui/unboxed-closures/unboxed-closures-borrow-conflict.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that an unboxed closure that mutates a free variable will
// cause borrow conflicts.



fn main() {
    let mut x = 0;
    let f = || x += 1;
    let _y = x; //~ ERROR cannot use `x` because it was mutably borrowed
    f;
}


