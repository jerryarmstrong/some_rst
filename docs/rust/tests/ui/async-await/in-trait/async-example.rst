tests/ui/async-await/in-trait/async-example.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition: 2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

trait MyTrait {
    async fn foo(&self) -> i32;
    async fn bar(&self) -> i32;
}

impl MyTrait for i32 {
    async fn foo(&self) -> i32 {
        *self
    }

    async fn bar(&self) -> i32 {
        self.foo().await
    }
}

fn main() {
    let x = 5;
    // Calling from non-async context
    let _ = x.foo();
    let _ = x.bar();
    // Calling from async block in non-async context
    async {
        let _: i32 = x.foo().await;
        let _: i32 = x.bar().await;
    };
}


