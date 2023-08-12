tests/ui/async-await/multiple-lifetimes/named.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// run-pass

// Test that we can use async fns with multiple arbitrary lifetimes.

async fn multiple_named_lifetimes<'a, 'b>(_: &'a u8, _: &'b u8) {}

fn main() {
    let _ = multiple_named_lifetimes(&22, &44);
}


