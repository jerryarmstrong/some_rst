tests/ui/impl-trait/in-trait/opaque-in-impl-is-opaque.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

use std::fmt::Display;

trait Foo {
    fn bar(&self) -> impl Display;
}

impl Foo for () {
    fn bar(&self) -> impl Display {
        "Hello, world"
    }
}

fn main() {
    let x: &str = ().bar();
    //~^ ERROR mismatched types
}


