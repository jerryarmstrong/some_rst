tests/ui/borrowck/index-mut-help-with-impl.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // When mutably indexing a type that implements `Index` and `IndexMut` but
// `Index::index` is being used specifically, the normal special help message
// should not mention a missing `IndexMut` impl.

fn main() {
    use std::ops::Index;

    let v = String::from("dinosaur");
    Index::index(&v, 1..2).make_ascii_uppercase(); //~ ERROR
}


