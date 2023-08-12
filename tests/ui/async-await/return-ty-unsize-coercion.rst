tests/ui/async-await/return-ty-unsize-coercion.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we apply unsizing coercions based on the return type.
//
// Also serves as a regression test for #60424.
//
// edition:2018
// check-pass

#![allow(warnings)]

use std::fmt::Debug;

// Unsizing coercion from `Box<&'static str>` to `Box<dyn Debug>`.
fn unsize_trait_coercion() {
    fn sync_example() -> Box<dyn Debug> {
        Box::new("asdf")
    }

    async fn async_example() -> Box<dyn Debug> {
        Box::new("asdf")
    }
}

// Unsizing coercion from `Box<[u32; N]>` to `Box<[32]>`.
fn unsize_slice_coercion() {
    fn sync_example() -> Box<[u32]> {
        Box::new([0])
    }

    async fn async_example() -> Box<[u32]> {
        Box::new([0])
    }
}

// Unsizing coercion from `&[&str; 1]` to `&[&str]`
fn unsize_slice_str_coercion() {
    fn sync_example() -> &'static [&'static str] {
        &["hi"]
    }

    async fn async_example() -> &'static [&'static str] {
        &["hi"]
    }
}

fn main() {}


