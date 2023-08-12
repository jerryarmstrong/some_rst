tests/ui/async-await/issue-67252-unnamed-future.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};

fn spawn<T: Send>(_: T) {}

pub struct AFuture;
impl Future for AFuture{
    type Output = ();

    fn poll(mut self: Pin<&mut Self>, _: &mut Context<'_>) -> Poll<()> {
        unimplemented!()
    }
}

async fn foo() {
    spawn(async { //~ ERROR future cannot be sent between threads safely
        let _a = std::ptr::null_mut::<()>(); // `*mut ()` is not `Send`
        AFuture.await;
    });
}

fn main() {}


