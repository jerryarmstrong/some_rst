tests/ui/allocator/auxiliary/system-allocator.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![crate_type = "rlib"]

use std::alloc::System;

#[global_allocator]
static A: System = System;


