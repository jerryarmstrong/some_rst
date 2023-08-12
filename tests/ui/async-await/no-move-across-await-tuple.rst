tests/ui/async-await/no-move-across-await-tuple.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// compile-flags: --crate-type lib

async fn no_move_across_await_tuple() -> Vec<usize> {
    let x = (vec![3], vec![4, 4]);
    drop(x.1);
    nothing().await;
    x.1
    //~^ ERROR use of moved value: `x.1`
}

async fn nothing() {}


