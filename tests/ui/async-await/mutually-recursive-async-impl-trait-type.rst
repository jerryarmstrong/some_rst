tests/ui/async-await/mutually-recursive-async-impl-trait-type.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// Test that impl trait does not allow creating recursive types that are
// otherwise forbidden when using `async` and `await`.

async fn rec_1() { //~ ERROR recursion in an `async fn`
    rec_2().await;
}

async fn rec_2() { //~ ERROR recursion in an `async fn`
    rec_1().await;
}

fn main() {}


