tests/ui/lint/must_not_suspend/dedup.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![feature(must_not_suspend)]
#![deny(must_not_suspend)]

#[must_not_suspend]
struct No {}

async fn shushspend() {}

async fn wheeee<T>(t: T) {
    shushspend().await;
    drop(t);
}

async fn yes() {
    wheeee(&No {}).await; //~ ERROR `No` held across
}

fn main() {
}


