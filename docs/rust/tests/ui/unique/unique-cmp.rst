tests/ui/unique/unique-cmp.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_allocation)]

pub fn main() {
    let i: Box<_> = Box::new(100);
    assert_eq!(i, Box::new(100));
    assert!(i < Box::new(101));
    assert!(i <= Box::new(100));
    assert!(i > Box::new(99));
    assert!(i >= Box::new(99));
}


