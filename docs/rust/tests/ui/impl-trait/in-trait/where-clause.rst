tests/ui/impl-trait/in-trait/where-clause.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition: 2021

#![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

use std::fmt::Debug;

trait Foo<Item> {
    fn foo<'a>(&'a self) -> impl Debug
    where
        Item: 'a;
}

impl<Item, D: Debug + Clone> Foo<Item> for D {
    fn foo<'a>(&'a self) -> impl Debug
    where
        Item: 'a,
    {
        self.clone()
    }
}

fn main() {}


