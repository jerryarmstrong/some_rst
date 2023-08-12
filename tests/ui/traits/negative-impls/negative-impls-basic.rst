tests/ui/traits/negative-impls/negative-impls-basic.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // A simple test that we are able to create negative impls, when the
// feature gate is given.
//
// run-pass

#![feature(negative_impls)]
#![allow(dead_code)]

struct TestType;

trait TestTrait {
    fn dummy(&self) {}
}

impl !TestTrait for TestType {}

fn main() {}


