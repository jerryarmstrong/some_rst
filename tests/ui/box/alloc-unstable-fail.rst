tests/ui/box/alloc-unstable-fail.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::boxed::Box;

fn main() {
    let _boxed: Box<u32, _> = Box::new(10);
    //~^ ERROR use of unstable library feature 'allocator_api'
}


