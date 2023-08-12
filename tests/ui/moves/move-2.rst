tests/ui/moves/move-2.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

struct X { x: isize, y: isize, z: isize }

pub fn main() { let x: Box<_> = Box::new(X {x: 1, y: 2, z: 3}); let y = x; assert_eq!(y.y, 2); }


