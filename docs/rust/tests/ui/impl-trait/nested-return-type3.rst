tests/ui/impl-trait/nested-return-type3.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Duh {}

impl Duh for i32 {}

trait Trait {
    type Assoc: Duh;
}

impl<F: Duh> Trait for F {
    type Assoc = F;
}

fn foo() -> impl Trait<Assoc = impl Send> {
    //~^ WARN opaque type `impl Trait<Assoc = impl Send>` does not satisfy its associated type bounds
    42
}

fn main() {
}


