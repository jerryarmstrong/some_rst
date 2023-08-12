tests/ui/consts/miri_unleashed/box.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you
#![feature(box_syntax)]

use std::mem::ManuallyDrop;

fn main() {}

static TEST_BAD: &mut i32 = {
    &mut *(box 0)
    //~^ ERROR could not evaluate static initializer
    //~| NOTE calling non-const function `alloc::alloc::exchange_malloc`
};


