tests/ui/single-use-lifetime/two-uses-in-trait-impl.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we DO NOT warn for a lifetime on an impl used in both
// header and in an associated type.
//
// check-pass

#![deny(single_use_lifetimes)]
#![allow(dead_code)]
#![allow(unused_variables)]

struct Foo<'f> {
    data: &'f u32,
}

impl<'f> Iterator for Foo<'f> {
    type Item = &'f u32;

    fn next(&mut self) -> Option<Self::Item> {
        None
    }
}

fn main() {}


