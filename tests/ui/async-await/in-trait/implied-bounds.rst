tests/ui/async-await/in-trait/implied-bounds.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition: 2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

trait TcpStack {
    type Connection<'a>: Sized where Self: 'a;
    fn connect<'a>(&'a self) -> Self::Connection<'a>;
    async fn async_connect<'a>(&'a self) -> Self::Connection<'a>;
}

fn main() {}


