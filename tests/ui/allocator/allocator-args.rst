tests/ui/allocator/allocator-args.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::alloc::{GlobalAlloc, Layout};

struct A;

unsafe impl GlobalAlloc for A {
    unsafe fn alloc(&self, _: Layout) -> *mut u8 { panic!() }
    unsafe fn dealloc(&self, _: *mut u8, _: Layout) { panic!() }
}

#[global_allocator(malloc)] //~ ERROR malformed `global_allocator` attribute input
static S: A = A;

fn main() {}


