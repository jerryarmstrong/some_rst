tests/ui/regions/regions-outlives-scalar.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that scalar values outlive all regions.
// Rule OutlivesScalar from RFC 1214.

// check-pass
#![allow(dead_code)]

struct Foo<'a> {
    x: &'a i32,
    y: &'static i32
}


fn main() { }


