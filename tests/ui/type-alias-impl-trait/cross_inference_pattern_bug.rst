tests/ui/type-alias-impl-trait/cross_inference_pattern_bug.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition=2021
// check-pass
#![feature(type_alias_impl_trait)]

fn main() {
    type T = impl Copy;
    let foo: T = (1u32, 2u32);
    let (a, b): (u32, u32) = foo;
}


