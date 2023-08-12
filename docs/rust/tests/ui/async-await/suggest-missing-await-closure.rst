tests/ui/async-await/suggest-missing-await-closure.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// run-rustfix

#![feature(async_closure)]

fn take_u32(_x: u32) {}

async fn make_u32() -> u32 {
    22
}

#[allow(unused)]
async fn suggest_await_in_async_closure() {
    async || {
        let x = make_u32();
        take_u32(x)
        //~^ ERROR mismatched types [E0308]
        //~| HELP consider `await`ing on the `Future`
        //~| SUGGESTION .await
    };
}

fn main() {}


