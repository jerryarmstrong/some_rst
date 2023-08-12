tests/ui/cycle-trait/cycle-trait-default-type-trait.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test a cycle where a type parameter on a trait has a default that
// again references the trait.

trait Foo<X = Box<dyn Foo>> {
    //~^ ERROR cycle detected
}

fn main() { }


