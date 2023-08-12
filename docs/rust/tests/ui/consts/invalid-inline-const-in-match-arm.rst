tests/ui/consts/invalid-inline-const-in-match-arm.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(incomplete_features)]
#![feature(inline_const_pat)]

fn main() {
    match () {
        const { (|| {})() } => {}
        //~^ ERROR cannot call non-const closure in constants
    }
}


