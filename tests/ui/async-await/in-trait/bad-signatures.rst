tests/ui/async-await/in-trait/bad-signatures.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(async_fn_in_trait)]
//~^ WARN the feature `async_fn_in_trait` is incomplete

trait MyTrait {
    async fn bar(&abc self);
    //~^ ERROR expected identifier, found keyword `self`
    //~| ERROR expected one of `:`, `@`, or `|`, found keyword `self`
}

impl MyTrait for () {
    async fn bar(&self) {}
}

fn main() {}


