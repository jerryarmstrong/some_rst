tests/ui/unique/unique-move-temp.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]

pub fn main() {
    let mut i: Box<_>;
    i = Box::new(100);
    assert_eq!(*i, 100);
}


