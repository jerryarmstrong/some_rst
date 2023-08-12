tests/ui/async-await/issue-63832-await-short-temporary-lifetime.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018

async fn foo(x: &[Vec<u32>]) -> u32 {
    0
}

async fn bar() {
    foo(&[vec![123]]).await;
}

fn main() { }


