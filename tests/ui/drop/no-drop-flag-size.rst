tests/ui/drop/no-drop-flag-size.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
use std::mem::size_of;

struct Test<T> {
    a: T
}

impl<T> Drop for Test<T> {
    fn drop(&mut self) { }
}

pub fn main() {
    assert_eq!(size_of::<isize>(), size_of::<Test<isize>>());
}


