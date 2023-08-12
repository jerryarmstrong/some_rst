tests/ui/not-panic/not-panic-safe.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use std::panic::UnwindSafe;

fn assert<T: UnwindSafe + ?Sized>() {}

fn main() {
    assert::<&mut &mut &i32>();
    //~^ ERROR the type `&mut &mut &i32` may not be safely transferred across an unwind boundary
}


