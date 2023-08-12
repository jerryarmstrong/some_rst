tests/ui/type-alias-impl-trait/collect_hidden_types.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:collect_hidden_types.rs
use collect_hidden_types::Service;
use std::future::Future;
use std::pin::Pin;
use std::task::Context;

// build-pass

// edition:2018

extern crate collect_hidden_types;

fn broken(mut a: collect_hidden_types::A, cx: &mut Context<'_>) {
    let mut fut = a.call(());
    let _ = unsafe { Pin::new_unchecked(&mut fut) }.poll(cx);
}

pub async fn meeb(cx: &mut Context<'_>) {
    broken(collect_hidden_types::A, cx);
}

fn main() {}


