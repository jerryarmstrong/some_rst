tests/ui/impl-trait/in-trait/deep-match.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

struct Wrapper<T>(T);

trait Foo {
    fn bar() -> Wrapper<impl Sized>;
}

impl Foo for () {
    fn bar() -> i32 { 0 }
    //~^ ERROR method `bar` has an incompatible return type for trait
}

fn main() {}


