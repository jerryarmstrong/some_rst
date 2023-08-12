tests/ui/async-await/multiple-lifetimes/hrtb.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

// Test that we can use async fns with multiple arbitrary lifetimes.

use std::ops::Add;

async fn multiple_hrtb_and_single_named_lifetime_ok<'c>(
    _: impl for<'a> Add<&'a u8>,
    _: impl for<'b> Add<&'b u8>,
    _: &'c u8,
) {}

fn main() {}


