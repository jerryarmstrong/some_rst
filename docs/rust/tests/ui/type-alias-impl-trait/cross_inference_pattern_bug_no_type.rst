tests/ui/type-alias-impl-trait/cross_inference_pattern_bug_no_type.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition=2021 --crate-type=lib
// rustc-env:RUST_BACKTRACE=0
// check-pass

// tracked in https://github.com/rust-lang/rust/issues/96572

#![feature(type_alias_impl_trait)]

fn main() {
    type T = impl Copy;
    let foo: T = (1u32, 2u32);
    let (a, b) = foo; // this line used to make the code fail
}


