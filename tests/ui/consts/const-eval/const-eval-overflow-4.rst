tests/ui/consts/const-eval/const-eval-overflow-4.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Evaluation of constants in array-elem count goes through different
// compiler control-flow paths.
//
// This test is checking the count in an array type.

#![allow(unused_imports)]

use std::fmt;

const A_I8_T
    : [u32; (i8::MAX as i8 + 1i8) as usize]
    //~^ ERROR evaluation of constant value failed
    = [0; (i8::MAX as usize) + 1];

fn main() {
    foo(&A_I8_T[..]);
}

fn foo<T:fmt::Debug>(x: T) {
    println!("{:?}", x);
}


