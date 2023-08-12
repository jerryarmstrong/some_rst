tests/ui/suggestions/missing-trait-item.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

trait T {
    unsafe fn foo(a: &usize, b: &usize) -> usize;
    fn bar(&self, a: &usize, b: &usize) -> usize;
}

mod foo {
    use super::T;
    impl T for () {} //~ ERROR not all trait items

    impl T for usize { //~ ERROR not all trait items
    }
}

fn main() {}


