tests/ui/rust-2018/uniform-paths/ambiguity-nested.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// This test is similar to `ambiguity.rs`, but nested in a module.

#![allow(non_camel_case_types)]

mod foo {
    pub use std::io;
    //~^ ERROR `std` is ambiguous

    mod std {
        pub struct io;
    }
}

fn main() {}


