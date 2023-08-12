tests/ui/async-await/multiple-lifetimes/elided.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// run-pass

// Test that we can use async fns with multiple arbitrary lifetimes.

async fn multiple_elided_lifetimes(_: &u8, _: &u8) {}

fn main() {
    let _ = multiple_elided_lifetimes(&22, &44);
}


