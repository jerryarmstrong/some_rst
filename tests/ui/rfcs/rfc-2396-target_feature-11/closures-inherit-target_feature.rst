tests/ui/rfcs/rfc-2396-target_feature-11/closures-inherit-target_feature.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests #73631: closures inherit `#[target_feature]` annotations

// check-pass
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck
// only-x86_64

#![feature(target_feature_11)]

#[target_feature(enable="avx")]
fn also_use_avx() {
    println!("Hello from AVX")
}

#[target_feature(enable="avx")]
fn use_avx() -> Box<dyn Fn()> {
    Box::new(|| also_use_avx())
}

fn main() {}


