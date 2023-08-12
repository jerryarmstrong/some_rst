tests/ui/rfcs/rfc-2396-target_feature-11/fn-ptr.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck
// only-x86_64

#![feature(target_feature_11)]

#[target_feature(enable = "sse2")]
fn foo() {}

fn main() {
    let foo: fn() = foo; //~ ERROR mismatched types
}


