tests/ui/type-alias-impl-trait/auxiliary/cross_crate_ice2.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Crate that exports an opaque `impl Trait` type. Used for testing cross-crate.

#![crate_type = "rlib"]
#![feature(type_alias_impl_trait)]

pub trait View {
    type Tmp: Iterator<Item = u32>;

    fn test(&self) -> Self::Tmp;
}

pub struct X;

impl View for X {
    type Tmp = impl Iterator<Item = u32>;

    fn test(&self) -> Self::Tmp {
        vec![1, 2, 3].into_iter()
    }
}


