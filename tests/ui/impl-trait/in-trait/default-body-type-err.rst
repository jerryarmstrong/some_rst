tests/ui/impl-trait/in-trait/default-body-type-err.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(incomplete_features)]
#![feature(return_position_impl_trait_in_trait)]

use std::ops::Deref;

pub trait Foo {
    fn lol(&self) -> impl Deref<Target = String> {
        //~^ type mismatch resolving `<&i32 as Deref>::Target == String`
        &1i32
    }
}

fn main() {}


