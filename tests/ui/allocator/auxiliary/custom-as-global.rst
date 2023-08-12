tests/ui/allocator/auxiliary/custom-as-global.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![crate_type = "rlib"]

extern crate custom;

use std::sync::atomic::{AtomicUsize, Ordering};

use custom::A;

#[global_allocator]
static ALLOCATOR: A = A(AtomicUsize::new(0));

pub fn get() -> usize {
    ALLOCATOR.0.load(Ordering::SeqCst)
}


