tests/ui/allocator/two-allocators3.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:system-allocator.rs
// aux-build:system-allocator2.rs
// no-prefer-dynamic
// error-pattern: the `#[global_allocator]` in


extern crate system_allocator;
extern crate system_allocator2;

fn main() {}


