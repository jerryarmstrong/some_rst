tests/ui/async-await/in-trait/async-example-desugared-boxed-in-trait.rs
=======================================================================

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
    fn foo(&self) -> Pin<Box<dyn Future<Output = i32> + '_>>;
}

impl MyTrait for i32 {
    async fn foo(&self) -> i32 {
        //~^ ERROR method `foo` has an incompatible type for trait
        *self
    }
}

fn main() {}


