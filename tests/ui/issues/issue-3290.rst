tests/ui/issues/issue-3290.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

pub fn main() {
   let mut x: Box<_> = Box::new(3);
   x = x;
   assert_eq!(*x, 3);
}


