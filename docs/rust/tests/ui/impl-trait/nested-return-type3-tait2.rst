tests/ui/impl-trait/nested-return-type3-tait2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]

trait Duh {}

impl Duh for i32 {}

trait Trait {
    type Assoc: Duh;
}

impl<F: Duh> Trait for F {
    type Assoc = F;
}

type Sendable = impl Send;
type Traitable = impl Trait<Assoc = Sendable>;
//~^ WARN opaque type `Traitable` does not satisfy its associated type bounds

fn foo() -> Traitable {
    42
}

fn main() {
}


