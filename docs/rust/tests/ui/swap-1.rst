tests/ui/swap-1.rs
==================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::mem::swap;

pub fn main() {
    let mut x = 3; let mut y = 7;
    swap(&mut x, &mut y);
    assert_eq!(x, 7);
    assert_eq!(y, 3);
}


