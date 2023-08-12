tests/ui/rfc-2632-const-trait-impl/cross-crate-default-method-body-is-const.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This tests that `const_trait` default methods can
// be called from a const context when used across crates.
//
// check-pass

#![feature(const_trait_impl)]

// aux-build: cross-crate.rs
extern crate cross_crate;

use cross_crate::*;

const _: () = {
    Const.func();
    Const.defaulted_func();
};

fn main() {}


