tests/ui/async-await/issues/issue-65419/issue-65419-async-fn-resume-after-completion.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue 65419 - Attempting to run an async fn after completion mentions generators when it should
// be talking about `async fn`s instead.

// run-fail
// error-pattern: thread 'main' panicked at '`async fn` resumed after completion'
// edition:2018
// ignore-wasm no panic or subprocess support
// ignore-emscripten no panic or subprocess support

#![feature(generators, generator_trait)]

async fn foo() {
}

fn main() {
    let mut future = Box::pin(foo());
    executor::block_on(future.as_mut());
    executor::block_on(future.as_mut());
}

mod executor {
    use core::{
        future::Future,
        pin::Pin,
        task::{Context, Poll, RawWaker, RawWakerVTable, Waker},
    };

    pub fn block_on<F: Future>(mut future: F) -> F::Output {
        let mut future = unsafe { Pin::new_unchecked(&mut future) };

        static VTABLE: RawWakerVTable = RawWakerVTable::new(
            |_| unimplemented!("clone"),
            |_| unimplemented!("wake"),
            |_| unimplemented!("wake_by_ref"),
            |_| (),
        );
        let waker = unsafe { Waker::from_raw(RawWaker::new(core::ptr::null(), &VTABLE)) };
        let mut context = Context::from_waker(&waker);

        loop {
            if let Poll::Ready(val) = future.as_mut().poll(&mut context) {
                break val;
            }
        }
    }
}


