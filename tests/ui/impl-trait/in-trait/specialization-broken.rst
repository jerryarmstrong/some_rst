tests/ui/impl-trait/in-trait/specialization-broken.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // FIXME(compiler-errors): I'm not exactly sure if this is expected to pass or not.
// But we fixed an ICE anyways.

#![feature(specialization)]
#![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

trait Foo {
    fn bar(&self) -> impl Sized;
}

default impl<U> Foo for U
where
    U: Copy,
{
    fn bar(&self) -> U {
        //~^ ERROR method `bar` has an incompatible type for trait
        *self
    }
}

impl Foo for i32 {}

fn main() {
    1i32.bar();
}


