tests/ui/borrowck/lazy-init.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_mut)]


fn foo(x: isize) { println!("{}", x); }

pub fn main() { let mut x: isize; if 1 > 2 { x = 12; } else { x = 10; } foo(x); }


