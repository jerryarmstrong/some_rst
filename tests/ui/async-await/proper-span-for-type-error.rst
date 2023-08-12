tests/ui/async-await/proper-span-for-type-error.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// run-rustfix
#![allow(dead_code)]

async fn a() {}

async fn foo() -> Result<(), i32> {
    a().await //~ ERROR mismatched types
}

fn main() {}


