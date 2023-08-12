tests/run-make-fulldeps/issue-69368/b.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]
#![feature(alloc_error_handler)]
#![no_std]

#[alloc_error_handler]
pub fn error_handler(_: core::alloc::Layout) -> ! {
    panic!();
}


