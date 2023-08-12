tests/ui/rust-2021/inherent-method-collision.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we do NOT warn for inherent methods invoked via `T::` form.
//
// check-pass

#![deny(rust_2021_prelude_collisions)]

pub struct MySeq {}

impl MySeq {
    pub fn from_iter(_: impl IntoIterator<Item = u32>) {}
}

fn main() {
    MySeq::from_iter(Some(22));
}


