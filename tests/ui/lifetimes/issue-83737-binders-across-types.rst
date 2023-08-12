tests/ui/lifetimes/issue-83737-binders-across-types.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// compile-flags: --edition 2018
// compile-flags: --crate-type rlib

use std::future::Future;

async fn handle<F>(slf: &F)
where
    F: Fn(&()) -> Box<dyn Future<Output = ()> + Unpin>,
{
    (slf)(&()).await;
}

fn main() {}


