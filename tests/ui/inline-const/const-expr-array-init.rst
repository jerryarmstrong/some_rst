tests/ui/inline-const/const-expr-array-init.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

#![feature(inline_const)]

use std::cell::Cell;

fn main() {
    let _x = [const { Cell::new(0) }; 20];
}


