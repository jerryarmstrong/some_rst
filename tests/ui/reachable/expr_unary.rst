tests/ui/reachable/expr_unary.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
#![allow(unused_variables)]
#![allow(unused_assignments)]
#![allow(dead_code)]
#![deny(unreachable_code)]

fn foo() {
    let x: ! = * { return; }; //~ ERROR unreachable
    //~| ERROR type `!` cannot be dereferenced
}

fn main() { }


