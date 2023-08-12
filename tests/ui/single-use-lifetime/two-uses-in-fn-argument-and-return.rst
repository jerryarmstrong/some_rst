tests/ui/single-use-lifetime/two-uses-in-fn-argument-and-return.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we DO NOT warn when lifetime name is used in
// both the argument and return.
//
// check-pass

#![deny(single_use_lifetimes)]
#![allow(dead_code)]
#![allow(unused_variables)]

// OK: used twice
fn c<'a>(x: &'a u32) -> &'a u32 {
    &22
}

fn main() {}


