tests/ui/reachable/expr_box.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_syntax)]
#![allow(unused_variables)]
#![deny(unreachable_code)]

fn main() {
    let x = box return; //~ ERROR unreachable
    println!("hi");
}


