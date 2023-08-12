tests/ui/not-panic/not-panic-safe-2.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use std::panic::UnwindSafe;
use std::rc::Rc;
use std::cell::RefCell;

fn assert<T: UnwindSafe + ?Sized>() {}

fn main() {
    assert::<Rc<RefCell<i32>>>();
    //~^ ERROR the type `UnsafeCell<i32>` may contain interior mutability and a
    //~| ERROR the type `UnsafeCell<isize>` may contain interior mutability and a
}


