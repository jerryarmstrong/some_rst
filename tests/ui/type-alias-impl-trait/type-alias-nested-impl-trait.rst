tests/ui/type-alias-impl-trait/type-alias-nested-impl-trait.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(type_alias_impl_trait)]

use std::iter::{once, Chain};

type I<A> = Chain<A, impl Iterator<Item = &'static str>>;
fn test2<A: Iterator<Item = &'static str>>(x: A) -> I<A> {
    x.chain(once("5"))
}

fn main() {
    assert_eq!(vec!["1", "3", "5"], test2(["1", "3"].iter().cloned()).collect::<Vec<_>>());
}


