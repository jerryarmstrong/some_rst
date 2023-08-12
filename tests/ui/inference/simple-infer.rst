tests/ui/inference/simple-infer.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_mut)]


pub fn main() { let mut n; n = 1; println!("{}", n); }


