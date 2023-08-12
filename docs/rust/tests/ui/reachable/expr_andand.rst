tests/ui/reachable/expr_andand.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![allow(unused_variables)]
#![allow(dead_code)]
#![deny(unreachable_code)]

fn foo() {
    // No error here.
    let x = false && (return);
    println!("I am not dead.");
}

fn main() { }


