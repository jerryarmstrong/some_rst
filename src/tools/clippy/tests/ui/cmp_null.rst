src/tools/clippy/tests/ui/cmp_null.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::cmp_null)]
#![allow(unused_mut)]

use std::ptr;

fn main() {
    let x = 0;
    let p: *const usize = &x;
    if p == ptr::null() {
        println!("This is surprising!");
    }
    let mut y = 0;
    let mut m: *mut usize = &mut y;
    if m == ptr::null_mut() {
        println!("This is surprising, too!");
    }
}


