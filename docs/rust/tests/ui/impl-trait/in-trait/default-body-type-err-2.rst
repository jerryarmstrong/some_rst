tests/ui/impl-trait/in-trait/default-body-type-err-2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![allow(incomplete_features)]
#![feature(async_fn_in_trait)]

pub trait Foo {
    async fn woopsie_async(&self) -> String {
        42
        //~^ ERROR mismatched types
    }
}

fn main() {}


