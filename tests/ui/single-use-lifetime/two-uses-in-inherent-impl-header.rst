tests/ui/single-use-lifetime/two-uses-in-inherent-impl-header.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we DO NOT warn for a lifetime used twice in an impl.
//
// check-pass

#![deny(single_use_lifetimes)]
#![allow(dead_code)]
#![allow(unused_variables)]

struct Foo<'f> {
    data: &'f u32,
}

impl<'f> Foo<'f> {
    fn inherent_a(&self, data: &'f u32) {}
}

fn main() {}


