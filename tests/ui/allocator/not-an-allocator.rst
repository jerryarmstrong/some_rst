tests/ui/allocator/not-an-allocator.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[global_allocator]
static A: usize = 0;
//~^ ERROR E0277
//~| ERROR E0277
//~| ERROR E0277
//~| ERROR E0277

fn main() {}


