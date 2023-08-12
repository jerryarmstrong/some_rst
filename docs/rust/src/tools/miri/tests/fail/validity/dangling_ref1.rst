src/tools/miri/tests/fail/validity/dangling_ref1.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we catch this even without Stacked Borrows
//@compile-flags: -Zmiri-disable-stacked-borrows
use std::mem;

fn main() {
    let _x: &i32 = unsafe { mem::transmute(16usize) }; //~ ERROR: encountered a dangling reference (address 0x10 is unallocated)
}


