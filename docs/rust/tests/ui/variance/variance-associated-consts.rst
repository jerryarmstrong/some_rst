tests/ui/variance/variance-associated-consts.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the variance computation considers types that
// appear in const expressions to be invariant.

#![feature(rustc_attrs)]
#![allow(incomplete_features)]
#![feature(generic_const_exprs)]

trait Trait {
    const Const: usize;
}

#[rustc_variance]
struct Foo<T: Trait> { //~ ERROR [o]
    field: [u8; <T as Trait>::Const]
}

fn main() { }


