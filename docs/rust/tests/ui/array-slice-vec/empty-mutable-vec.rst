tests/ui/array-slice-vec/empty-mutable-vec.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// pretty-expanded FIXME #23616

#![allow(unused_mut)]


pub fn main() { let mut _v: Vec<isize> = Vec::new(); }


