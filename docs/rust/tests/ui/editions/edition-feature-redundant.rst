tests/ui/editions/edition-feature-redundant.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

#![feature(rust_2018_preview)]
//~^ WARN the feature `rust_2018_preview` is included in the Rust 2018 edition

fn main() {}


