tests/ui/self/self-re-assign.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Ensure assigning an owned or managed variable to itself works. In particular,
// that we do not glue_drop before we glue_take (#3290).

#![allow(dead_code)]

use std::rc::Rc;

pub fn main() {
   let mut x: Box<_> = Box::new(3);
   x = x;
   assert_eq!(*x, 3);

   let mut x = Rc::new(3);
   x = x;
   assert_eq!(*x, 3);
}


