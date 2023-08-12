tests/ui/async-await/unreachable-lint-1.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![deny(unreachable_code)]

async fn foo() {
    return; bar().await;
    //~^ ERROR unreachable statement
}

async fn bar() {
}

fn main() { }


