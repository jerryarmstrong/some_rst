tests/ui/async-await/unreachable-lint.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018
#![deny(unreachable_code)]

async fn foo() {
    endless().await;
}

async fn endless() -> ! {
    loop {}
}

fn main() { }


