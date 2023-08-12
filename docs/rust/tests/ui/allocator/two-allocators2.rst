tests/ui/allocator/two-allocators2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:system-allocator.rs
// no-prefer-dynamic
// error-pattern: the `#[global_allocator]` in

extern crate system_allocator;

use std::alloc::System;

#[global_allocator]
static A: System = System;

fn main() {}


