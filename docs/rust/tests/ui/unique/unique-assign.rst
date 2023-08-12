tests/ui/unique/unique-assign.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]

pub fn main() {
    let mut i: Box<_>;
    i = Box::new(1);
    assert_eq!(*i, 1);
}


