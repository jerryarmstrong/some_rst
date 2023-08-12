tests/ui/not-panic/not-panic-safe-5.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use std::panic::UnwindSafe;
use std::cell::UnsafeCell;

fn assert<T: UnwindSafe + ?Sized>() {}

fn main() {
    assert::<*const UnsafeCell<i32>>(); //~ ERROR E0277
}


