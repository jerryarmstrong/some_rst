tests/ui/async-await/no-std.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

#![no_std]
#![crate_type = "rlib"]

use core::future::Future;

async fn a(f: impl Future) {
    f.await;
}

fn main() {}


