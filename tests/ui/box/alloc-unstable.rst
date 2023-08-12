tests/ui/box/alloc-unstable.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(allocator_api)]

use std::boxed::Box;

fn main() {
    let _boxed: Box<u32, _> = Box::new(10);
}


