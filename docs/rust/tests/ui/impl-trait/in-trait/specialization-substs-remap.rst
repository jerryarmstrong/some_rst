tests/ui/impl-trait/in-trait/specialization-substs-remap.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(specialization)]
#![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

trait Foo {
    fn bar(&self) -> impl Sized;
}

impl<U> Foo for U
where
    U: Copy,
{
    fn bar(&self) -> U {
        *self
    }
}

impl Foo for i32 {}

fn main() {
    let _: i32 = 1i32.bar();
}


