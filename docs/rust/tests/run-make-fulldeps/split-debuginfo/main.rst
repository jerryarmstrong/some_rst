tests/run-make-fulldeps/split-debuginfo/main.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate bar;

use bar::{Bar, make_bar};

fn main() {
    let b = make_bar(3);
    b.print();
}


