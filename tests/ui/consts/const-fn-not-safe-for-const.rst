tests/ui/consts/const-fn-not-safe-for-const.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can't call random fns in a const fn or do other bad things.

use std::mem::transmute;

fn random() -> u32 {
    0
}

const fn sub(x: &u32) -> usize {
    unsafe { transmute(x) }
}

const fn sub1() -> u32 {
    random() //~ ERROR E0015
}

static Y: u32 = 0;

const fn get_Y() -> u32 {
    Y
    //~^ ERROR E0013
}

const fn get_Y_addr() -> &'static u32 {
    &Y
    //~^ ERROR E0013
}

const fn get() -> u32 {
    let x = 22;
    let y = 44;
    x + y
}

fn main() {}


