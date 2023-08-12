tests/pretty/async.rs
=====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact
// pretty-compare-only
// edition:2021

async fn f() {
    let first = async { 1 };
    let second = async move { 2 };
    join(first, second).await
}


