tests/ui/async-await/in-trait/async-recursive.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition: 2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

trait MyTrait {
    async fn foo_recursive(&self, n: usize) -> i32;
}

impl MyTrait for i32 {
    async fn foo_recursive(&self, n: usize) -> i32 {
        //~^ ERROR recursion in an `async fn` requires boxing
        if n > 0 {
            self.foo_recursive(n - 1).await
        } else {
            *self
        }
    }
}

fn main() {}


