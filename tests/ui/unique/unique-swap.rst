tests/ui/unique/unique-swap.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::mem::swap;

pub fn main() {
    let mut i: Box<_> = Box::new(100);
    let mut j: Box<_> = Box::new(200);
    swap(&mut i, &mut j);
    assert_eq!(i, Box::new(200));
    assert_eq!(j, Box::new(100));
}


