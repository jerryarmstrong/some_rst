tests/ui/async-await/in-trait/async-example-desugared-boxed.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition: 2021

#![feature(async_fn_in_trait)]
#![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

use std::future::Future;
use std::pin::Pin;

trait MyTrait {
    async fn foo(&self) -> i32;
}

impl MyTrait for i32 {
    fn foo(&self) -> Pin<Box<dyn Future<Output = i32> + '_>> {
        //~^ ERROR method `foo` should be async
        Box::pin(async { *self })
    }
}

fn main() {}


