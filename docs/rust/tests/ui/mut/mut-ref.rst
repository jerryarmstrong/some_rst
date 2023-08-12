tests/ui/mut/mut-ref.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut ref x = 10; //~ ERROR the order of `mut` and `ref` is incorrect
    let ref mut y = 11;
}


