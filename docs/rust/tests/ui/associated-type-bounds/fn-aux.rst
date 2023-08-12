tests/ui/associated-type-bounds/fn-aux.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:fn-aux.rs

#![feature(associated_type_bounds)]

extern crate fn_aux;

use fn_aux::*;

fn main() {
    desugared();
}


