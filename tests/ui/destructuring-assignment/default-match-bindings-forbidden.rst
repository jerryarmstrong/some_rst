tests/ui/destructuring-assignment/default-match-bindings-forbidden.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut x = &0;
    let mut y = &0;
    (x, y) = &(1, 2); //~ ERROR mismatched types
}


