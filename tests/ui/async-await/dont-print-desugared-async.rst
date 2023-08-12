tests/ui/async-await/dont-print-desugared-async.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we don't show variables with from async fn desugaring

// edition:2018

async fn async_fn(&ref mut s: &[i32]) {}
//~^ ERROR cannot borrow data in a `&` reference as mutable [E0596]

fn main() {}


