tests/ui/async-await/return-ty-raw-ptr-coercion.rs
==================================================

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

const TMP: u32 = 22;

// Coerce from `&u32` to `*const u32`
fn raw_pointer_coercion() {
    fn sync_example() -> *const u32 {
        &TMP
    }

    async fn async_example() -> *const u32 {
        &TMP
    }
}

fn main() {}


