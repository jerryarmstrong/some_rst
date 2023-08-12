tests/ui/unique/unique-move.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]

pub fn main() {
    let i: Box<_> = Box::new(100);
    let mut j;
    j = i;
    assert_eq!(*j, 100);
}


