tests/ui/borrowck/borrowck-while-cond.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: bool;
    while x { } //~ ERROR E0381
}


