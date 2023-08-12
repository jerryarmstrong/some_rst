tests/ui/suggestions/async-fn-ctor-passed-as-arg-where-it-should-have-been-called.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![feature(async_closure)]
use std::future::Future;

async fn foo() {}

fn bar(f: impl Future<Output=()>) {}

fn main() {
    bar(foo); //~ERROR E0277
    let async_closure = async || ();
    bar(async_closure); //~ERROR E0277
}


