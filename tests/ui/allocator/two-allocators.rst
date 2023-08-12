tests/ui/allocator/two-allocators.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::alloc::System;

#[global_allocator]
static A: System = System;
#[global_allocator]
static B: System = System;
//~^ ERROR: cannot define multiple global allocators

fn main() {}


