tests/ui/print_type_sizes/async.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z print-type-sizes --crate-type lib
// edition:2021
// build-pass
// ignore-pass

async fn wait() {}

pub async fn test(arg: [u8; 8192]) {
    wait().await;
    drop(arg);
}


