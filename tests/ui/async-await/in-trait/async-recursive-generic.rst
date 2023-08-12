tests/ui/async-await/in-trait/async-recursive-generic.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition: 2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

trait MyTrait<T> {
    async fn foo_recursive(&self, n: usize) -> T;
}

impl<T> MyTrait<T> for T where T: Copy {
    async fn foo_recursive(&self, n: usize) -> T {
        //~^ ERROR recursion in an `async fn` requires boxing
        if n > 0 {
            self.foo_recursive(n - 1).await
        } else {
            *self
        }
    }
}

fn main() {}


