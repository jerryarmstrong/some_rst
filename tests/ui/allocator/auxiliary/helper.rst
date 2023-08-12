tests/ui/allocator/auxiliary/helper.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![crate_type = "rlib"]
#![no_std]

extern crate alloc;
use alloc::fmt;

pub fn work_with(p: &fmt::Debug) {
    drop(p);
}


