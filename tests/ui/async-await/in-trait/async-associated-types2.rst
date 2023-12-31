tests/ui/async-await/in-trait/async-associated-types2.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition: 2021

#![feature(async_fn_in_trait)]
#![feature(type_alias_impl_trait)]
#![allow(incomplete_features)]

use std::future::Future;

trait MyTrait {
    type Fut<'a>: Future<Output = i32>
    where
        Self: 'a;

    fn foo<'a>(&'a self) -> Self::Fut<'a>;
}

impl MyTrait for i32 {
    type Fut<'a> = impl Future<Output = i32> + 'a
    where
        Self: 'a;

    fn foo<'a>(&'a self) -> Self::Fut<'a> {
        async {
            *self
        }
    }
}

fn main() {}


