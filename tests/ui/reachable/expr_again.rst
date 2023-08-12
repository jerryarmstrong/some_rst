tests/ui/reachable/expr_again.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_variables)]

#![deny(unreachable_code)]

fn main() {
    let x = loop {
        continue;
        println!("hi");
        //~^ ERROR unreachable statement
    };
}


