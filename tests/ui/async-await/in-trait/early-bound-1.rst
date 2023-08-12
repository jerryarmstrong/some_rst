tests/ui/async-await/in-trait/early-bound-1.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

pub trait Foo {
    async fn foo(&mut self);
}

struct MyFoo<'a>(&'a mut ());

impl<'a> Foo for MyFoo<'a> {
    async fn foo(&mut self) {}
}

fn main() {}


