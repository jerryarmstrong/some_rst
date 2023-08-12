tests/ui/allocator/function-allocator.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[global_allocator]
fn foo() {} //~ ERROR: allocators must be statics

fn main() {}


