src/tools/miri/tests/fail/validity/dangling_ref3.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we catch this even without Stacked Borrows
//@compile-flags: -Zmiri-disable-stacked-borrows
use std::mem;

fn dangling() -> *const u8 {
    let x = 0u8;
    &x as *const _
}

fn main() {
    let _x: &i32 = unsafe { mem::transmute(dangling()) }; //~ ERROR: dangling reference (use-after-free)
}


