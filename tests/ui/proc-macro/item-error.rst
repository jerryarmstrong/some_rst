tests/ui/proc-macro/item-error.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:derive-b.rs

#![allow(warnings)]

#[macro_use]
extern crate derive_b;

#[derive(B)]
struct A {
    a: &u64
//~^ ERROR: missing lifetime specifier
}

fn main() {
}


