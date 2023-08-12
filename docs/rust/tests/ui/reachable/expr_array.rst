tests/ui/reachable/expr_array.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_variables)]
#![allow(unused_assignments)]
#![allow(dead_code)]
#![deny(unreachable_code)]
#![feature(type_ascription)]

fn a() {
    // the `22` is unreachable:
    let x: [usize; 2] = [return, 22]; //~ ERROR unreachable
}

fn b() {
    // the array is unreachable:
    let x: [usize; 2] = [22, return]; //~ ERROR unreachable
}

fn main() { }


