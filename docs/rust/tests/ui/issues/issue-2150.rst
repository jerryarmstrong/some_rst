tests/ui/issues/issue-2150.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_code)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn fail_len(v: Vec<isize> ) -> usize {
    let mut i = 3;
    panic!();
    for x in &v { i += 1; }
    //~^ ERROR: unreachable statement
    return i;
}
fn main() {}


