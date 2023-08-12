tests/ui/unique/unique-move-drop.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_variables)]

pub fn main() {
    let i: Box<_> = Box::new(100);
    let j: Box<_> = Box::new(200);
    let j = i;
    assert_eq!(*j, 100);
}


