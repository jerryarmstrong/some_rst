tests/ui/type-alias-impl-trait/future.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

// edition:2021
// compile-flags: --crate-type=lib

use std::future::Future;

trait Bar {
    fn bar(&self);
}

type FooFuture<B> = impl Future<Output = ()>;

fn foo<B: Bar>(bar: B) -> FooFuture<B> {
    async move { bar.bar() }
    //~^ ERROR: the trait bound `B: Bar` is not satisfied
}

pub fn mainish(ctx: &mut std::task::Context) {
    let boom: FooFuture<u32> = unsafe { core::mem::zeroed() };
    Box::pin(boom).as_mut().poll(ctx);
}


