tests/ui/async-await/in-trait/missing-send-bound.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(async_fn_in_trait)]
//~^ WARN the feature `async_fn_in_trait` is incomplete and may not be safe to use and/or cause compiler crashes

trait Foo {
    async fn bar();
}

async fn test<T: Foo>() {
    T::bar().await;
}

fn test2<T: Foo>() {
    assert_is_send(test::<T>());
    //~^ ERROR future cannot be sent between threads safely
}

fn assert_is_send(_: impl Send) {}

fn main() {}


