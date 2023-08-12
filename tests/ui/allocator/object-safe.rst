tests/ui/allocator/object-safe.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Check that `Allocator` is object safe, this allows for polymorphic allocators

#![feature(allocator_api)]

use std::alloc::{Allocator, System};

fn ensure_object_safe(_: &dyn Allocator) {}

fn main() {
    ensure_object_safe(&System);
}


