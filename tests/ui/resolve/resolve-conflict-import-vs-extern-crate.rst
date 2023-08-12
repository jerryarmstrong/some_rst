tests/ui/resolve/resolve-conflict-import-vs-extern-crate.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::slice as std; //~ ERROR the name `std` is defined multiple times

fn main() {
}


