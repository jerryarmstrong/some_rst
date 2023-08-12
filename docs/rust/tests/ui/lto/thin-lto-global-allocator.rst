tests/ui/lto/thin-lto-global-allocator.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Z thinlto -C codegen-units=2

#[global_allocator]
static A: std::alloc::System = std::alloc::System;

fn main() {}


