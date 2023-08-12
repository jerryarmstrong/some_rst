tests/ui/consts/const.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]

static i: isize = 10;

pub fn main() { println!("{}", i); }


