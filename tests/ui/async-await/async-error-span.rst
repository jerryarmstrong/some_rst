tests/ui/async-await/async-error-span.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// Regression test for issue #62382.

use std::future::Future;

fn get_future() -> impl Future<Output = ()> {
//~^ ERROR `()` is not a future
    panic!()
}

async fn foo() {
    let a; //~ ERROR type inside `async fn` body must be known in this context
    get_future().await;
}

fn main() {}


