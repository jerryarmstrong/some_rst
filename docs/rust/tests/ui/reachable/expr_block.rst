tests/ui/reachable/expr_block.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_variables)]
#![allow(unused_assignments)]
#![allow(dead_code)]
#![deny(unreachable_code)]

fn a() {
    // Here the tail expression is considered unreachable:
    let x = {
        return;
        22 //~ ERROR unreachable
    };
}

fn b() {
    // Here the `x` assignment is considered unreachable, not the block:
    let x = {
        return;
    };
}

fn c() {
    // Here the `println!` is unreachable:
    let x = {
        return;
        println!("foo");
        //~^ ERROR unreachable statement
        22
    };
}

fn main() { }


