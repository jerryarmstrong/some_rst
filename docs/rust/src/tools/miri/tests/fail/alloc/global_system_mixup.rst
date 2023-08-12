src/tools/miri/tests/fail/alloc/global_system_mixup.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we detect when the `Global` and `System` allocators are mixed
// (even when the default `Global` uses `System`).
//@error-pattern: /deallocating .*, which is Rust heap memory, using .* heap deallocation operation/

//@normalize-stderr-test: "using [A-Za-z]+ heap deallocation operation" -> "using PLATFORM heap deallocation operation"
//@normalize-stderr-test: "\| +\^+" -> "| ^"
//@normalize-stderr-test: "libc::free\([^()]*\)|unsafe \{ HeapFree\([^()]*\) \};" -> "FREE();"

#![feature(allocator_api, slice_ptr_get)]

use std::alloc::{Allocator, Global, Layout, System};

fn main() {
    let l = Layout::from_size_align(1, 1).unwrap();
    let ptr = Global.allocate(l).unwrap().as_non_null_ptr();
    unsafe {
        System.deallocate(ptr, l);
    }
}


