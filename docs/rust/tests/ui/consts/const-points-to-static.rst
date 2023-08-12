tests/ui/consts/const-points-to-static.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you
// stderr-per-bitwidth

#![allow(dead_code)]

const TEST: &u8 = &MY_STATIC;
//~^ ERROR it is undefined behavior to use this value
//~| encountered a reference pointing to a static variable

static MY_STATIC: u8 = 4;

fn main() {
}


