tests/ui/consts/miri_unleashed/raw_mutable_const.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you

use std::cell::UnsafeCell;

const MUTABLE_BEHIND_RAW: *mut i32 = &UnsafeCell::new(42) as *const _ as *mut _;
//~^ ERROR: untyped pointers are not allowed in constant

fn main() {}


