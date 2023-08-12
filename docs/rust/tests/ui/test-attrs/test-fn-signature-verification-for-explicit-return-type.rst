tests/ui/test-attrs/test-fn-signature-verification-for-explicit-return-type.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind (#73509)

#![feature(test)]

// compile-flags: --test
extern crate test;

#[bench]
pub fn bench_explicit_return_type(_: &mut ::test::Bencher) -> () {}

#[test]
pub fn test_explicit_return_type() -> () {}


