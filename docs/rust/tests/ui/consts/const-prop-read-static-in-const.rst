tests/ui/consts/const-prop-read-static-in-const.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you

#![allow(dead_code)]

const TEST: u8 = MY_STATIC; //~ ERROR constant

static MY_STATIC: u8 = 4;

fn main() {
}


