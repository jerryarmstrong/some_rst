tests/ui/impl-trait/in-trait/doesnt-satisfy.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

trait Foo {
    fn bar() -> impl std::fmt::Display;
}

impl Foo for () {
    fn bar() -> () {}
    //~^ ERROR `()` doesn't implement `std::fmt::Display`
}

fn main() {}


