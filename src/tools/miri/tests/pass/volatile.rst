src/tools/miri/tests/pass/volatile.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // related: #58645
#![feature(core_intrinsics)]
use std::intrinsics::{volatile_load, volatile_store};

pub fn main() {
    unsafe {
        let i: &mut (isize, isize) = &mut (0, 0);
        volatile_store(i, (1, 2));
        assert_eq!(volatile_load(i), (1, 2));
        assert_eq!(i, &mut (1, 2));
    }
}


