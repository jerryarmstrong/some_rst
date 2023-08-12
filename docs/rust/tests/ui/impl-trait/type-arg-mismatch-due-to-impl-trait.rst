tests/ui/impl-trait/type-arg-mismatch-due-to-impl-trait.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type T;
    fn foo(&self, t: Self::T);
//~^ NOTE expected 0 type parameters
}

impl Foo for u32 {
    type T = ();

    fn foo(&self, t: impl Clone) {}
//~^ ERROR method `foo` has 1 type parameter but its trait declaration has 0 type parameters
//~| NOTE found 1 type parameter
//~| NOTE `impl Trait` introduces an implicit type parameter
}

fn main() {}


