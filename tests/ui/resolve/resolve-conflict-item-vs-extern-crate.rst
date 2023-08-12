tests/ui/resolve/resolve-conflict-item-vs-extern-crate.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn std() {}
mod std {}    //~ ERROR the name `std` is defined multiple times

fn main() {
}


