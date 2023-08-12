tests/ui/hygiene/issue-77523-def-site-async-await.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// aux-build:opaque-hygiene.rs
// aux-build:def-site-async-await.rs

// Regression test for issue #77523
// Tests that we don't ICE when an unusual combination
// of def-site hygiene and cross-crate monomorphization occurs.

extern crate def_site_async_await;

use std::future::Future;

fn mk_ctxt() -> std::task::Context<'static> {
    panic!()
}

fn main() {
    Box::pin(def_site_async_await::serve()).as_mut().poll(&mut mk_ctxt());
}


