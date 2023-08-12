tests/ui/rust-2018/uniform-paths/ambiguity-macros.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// This test is similar to `ambiguity.rs`, but with macros defining local items.

#![allow(non_camel_case_types)]

use std::io;
//~^ ERROR `std` is ambiguous

macro_rules! m {
    () => {
        mod std {
            pub struct io;
        }
    }
}
m!();

fn main() {}


