tests/ui/traits/impl-method-mismatch.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Mumbo {
    fn jumbo(&self, x: &usize) -> usize;
}

impl Mumbo for usize {
    // Cannot have a larger effect than the trait:
    unsafe fn jumbo(&self, x: &usize) { *self + *x; }
    //~^ ERROR method `jumbo` has an incompatible type for trait
    //~| expected signature `fn
    //~| found signature `unsafe fn
}

fn main() {}


