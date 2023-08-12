tests/ui/resolve/resolve-conflict-import-vs-import.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[allow(unused_imports)]
use std::mem::transmute;
use std::mem::transmute;
//~^ ERROR the name `transmute` is defined multiple times

fn main() {
}


