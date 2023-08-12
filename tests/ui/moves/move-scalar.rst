tests/ui/moves/move-scalar.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]

pub fn main() {

    let y: isize = 42;
    let mut x: isize;
    x = y;
    assert_eq!(x, 42);
}


