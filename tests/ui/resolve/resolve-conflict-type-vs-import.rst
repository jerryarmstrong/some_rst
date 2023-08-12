tests/ui/resolve/resolve-conflict-type-vs-import.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::slice::Iter;

struct Iter;
//~^ ERROR the name `Iter` is defined multiple times

fn main() {
}


