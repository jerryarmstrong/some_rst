tests/ui/const-ptr/out_of_bounds_read.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: evaluation of constant value failed

#![feature(const_ptr_read)]

fn main() {
    use std::ptr;

    const DATA: [u32; 1] = [42];

    const PAST_END_PTR: *const u32 = unsafe { DATA.as_ptr().add(1) };

    const _READ: u32 = unsafe { ptr::read(PAST_END_PTR) };
    const _CONST_READ: u32 = unsafe { PAST_END_PTR.read() };
    const _MUT_READ: u32 = unsafe { (PAST_END_PTR as *mut u32).read() };
}


