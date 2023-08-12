tests/ui/consts/const-eval/const_panic_track_caller.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(non_fmt_panics)]
#![crate_type = "lib"]

#[track_caller]
const fn a() -> u32 {
    panic!("hey")
}

#[track_caller]
const fn b() -> u32 {
    a()
}

const fn c() -> u32 {
    b()
    //~^ ERROR evaluation of constant value failed
    //~| NOTE the evaluated program panicked
    //~| NOTE inside
}

const X: u32 = c();
//~^ NOTE inside


