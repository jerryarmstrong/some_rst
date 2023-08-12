tests/ui/type-alias-impl-trait/nested-tait-inference2.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![allow(dead_code)]

use std::fmt::Debug;

type FooX = impl Debug;

trait Foo<A> {}

impl Foo<()> for () {}
impl Foo<u32> for () {}

fn foo() -> impl Foo<FooX> {
    //~^ ERROR: the trait bound `(): Foo<FooX>` is not satisfied
    ()
}

fn main() {}


