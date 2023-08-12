tests/ui/impl-trait/impl-generic-mismatch-ab.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

trait Foo {
    fn foo<A: Debug>(&self, a: &A, b: &impl Debug);
}

impl Foo for () {
    fn foo<B: Debug>(&self, a: &impl Debug, b: &B) { }
    //~^ ERROR method `foo` has an incompatible type for trait
}

fn main() {}


