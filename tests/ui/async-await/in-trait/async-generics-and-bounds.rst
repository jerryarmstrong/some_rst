tests/ui/async-await/in-trait/async-generics-and-bounds.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
// known-bug: #102682
// edition: 2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

use std::fmt::Debug;
use std::hash::Hash;

trait MyTrait<T, U> {
    async fn foo(&self) -> &(T, U) where T: Debug + Sized, U: Hash;
}

impl<T, U> MyTrait<T, U> for (T, U) {
    async fn foo(&self) -> &(T, U) {
        self
    }
}

fn main() {}


