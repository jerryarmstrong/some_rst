tests/ui/consts/const-eval/const-eval-overflow-2.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Evaluation of constants in refutable patterns goes through
// different compiler control-flow paths.

#![allow(unused_imports, warnings)]

use std::fmt;
use std::{i8, i16, i32, i64, isize};
use std::{u8, u16, u32, u64, usize};

const NEG_128: i8 = -128;
const NEG_NEG_128: i8 = -NEG_128; //~ ERROR constant

fn main() {
    match -128i8 {
        NEG_NEG_128 => println!("A"),
        //~^ ERROR could not evaluate constant pattern
        //~| ERROR could not evaluate constant pattern
        _ => println!("B"),
    }
}


