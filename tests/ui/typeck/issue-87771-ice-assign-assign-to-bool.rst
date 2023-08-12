tests/ui/typeck/issue-87771-ice-assign-assign-to-bool.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut a;
    a = a = true; //~ ERROR mismatched types
}


