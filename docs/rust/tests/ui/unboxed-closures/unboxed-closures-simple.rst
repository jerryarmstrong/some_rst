tests/ui/unboxed-closures/unboxed-closures-simple.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]
#![allow(unused_imports)]
use std::ops::FnMut;

pub fn main() {
    let mut f = |x: isize, y: isize| -> isize { x + y };
    let z = f(1, 2);
    assert_eq!(z, 3);
}


