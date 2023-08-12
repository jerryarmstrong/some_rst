tests/run-make-fulldeps/std-core-cycle/bar.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(allocator_api)]
#![crate_type = "rlib"]

use std::alloc::*;

pub struct A;

unsafe impl GlobalAlloc for A {
    unsafe fn alloc(&self, _: Layout) -> *mut u8 {
        loop {}
    }

    unsafe fn dealloc(&self, _ptr: *mut u8, _: Layout) {
        loop {}
    }
}


