tests/ui/reachable/expr_repeat.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_variables)]
#![allow(unused_assignments)]
#![allow(dead_code)]
#![deny(unreachable_code)]
#![feature(type_ascription)]

fn a() {
    // the repeat is unreachable:
    let x: [usize; 2] = [return; 2]; //~ ERROR unreachable
}

fn main() { }


