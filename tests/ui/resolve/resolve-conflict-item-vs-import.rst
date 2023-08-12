tests/ui/resolve/resolve-conflict-item-vs-import.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem::transmute;

fn transmute() {}
//~^ ERROR the name `transmute` is defined multiple times
//~| `transmute` redefined here
//~| `transmute` must be defined only once in the value namespace of this module
fn main() {
}


