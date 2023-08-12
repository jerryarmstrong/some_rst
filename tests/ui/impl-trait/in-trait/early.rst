tests/ui/impl-trait/in-trait/early.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2021

#![feature(async_fn_in_trait, return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

pub trait Foo {
    async fn bar<'a: 'a>(&'a mut self);
}

impl Foo for () {
    async fn bar<'a: 'a>(&'a mut self) {}
}

pub trait Foo2 {
    fn bar<'a: 'a>(&'a mut self) -> impl Sized + 'a;
}

impl Foo2 for () {
    fn bar<'a: 'a>(&'a mut self) -> impl Sized + 'a {}
}

fn main() {}


