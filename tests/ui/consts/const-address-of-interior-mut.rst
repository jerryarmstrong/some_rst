tests/ui/consts/const-address-of-interior-mut.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(raw_ref_op)]

use std::cell::Cell;

const A: () = { let x = Cell::new(2); &raw const x; };      //~ ERROR interior mutability

static B: () = { let x = Cell::new(2); &raw const x; };     //~ ERROR interior mutability

static mut C: () = { let x = Cell::new(2); &raw const x; }; //~ ERROR interior mutability

const fn foo() {
    let x = Cell::new(0);
    let y = &raw const x;                                   //~ ERROR interior mutability
}

fn main() {}


