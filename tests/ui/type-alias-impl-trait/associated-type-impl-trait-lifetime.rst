tests/ui/type-alias-impl-trait/associated-type-impl-trait-lifetime.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //check-pass

#![feature(type_alias_impl_trait)]

trait Trait {
    type Opaque1;
    type Opaque2;
    fn constrain(self);
}

impl<'a> Trait for &'a () {
    type Opaque1 = impl Sized;
    type Opaque2 = impl Sized + 'a;
    fn constrain(self) {
        let _: Self::Opaque1 = ();
        let _: Self::Opaque2 = self;
    }
}

fn main() {}


