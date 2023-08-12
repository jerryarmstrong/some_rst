tests/ui/async-await/repeat_count_const_in_async_fn.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018
// compile-flags: --crate-type=lib

pub async fn test() {
    const C: usize = 4;
    foo(&mut [0u8; C]).await;
}

async fn foo(_: &mut [u8]) {}


