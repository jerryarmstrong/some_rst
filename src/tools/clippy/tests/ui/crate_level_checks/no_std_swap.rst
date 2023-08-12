src/tools/clippy/tests/ui/crate_level_checks/no_std_swap.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
#![feature(lang_items, start, libc)]
#![crate_type = "lib"]

use core::panic::PanicInfo;

#[warn(clippy::all)]
fn main() {
    let mut a = 42;
    let mut b = 1337;

    a = b;
    b = a;
}


