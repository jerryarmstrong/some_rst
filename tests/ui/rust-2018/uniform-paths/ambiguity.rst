tests/ui/rust-2018/uniform-paths/ambiguity.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![allow(non_camel_case_types)]

use std::io;
//~^ ERROR `std` is ambiguous

mod std {
    pub struct io;
}

fn main() {}


