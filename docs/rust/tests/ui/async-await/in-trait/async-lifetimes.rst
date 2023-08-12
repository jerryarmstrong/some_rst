tests/ui/async-await/in-trait/async-lifetimes.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition: 2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

trait MyTrait<'a, 'b, T> {
    async fn foo(&'a self, key: &'b T) -> (&'a Self, &'b T);
}

impl<'a, 'b, T, U> MyTrait<'a, 'b, T> for U {
    async fn foo(&'a self, key: &'b T) -> (&'a U, &'b T) {
        (self, key)
    }
}

fn main() {}


