tests/ui/borrowck/borrowck-and-init.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let i: isize;

    println!("{}", false && { i = 5; true });
    println!("{}", i); //~ ERROR E0381
}


