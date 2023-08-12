tests/ui/type-alias-impl-trait/auxiliary/cross_crate_ice.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Crate that exports an opaque `impl Trait` type. Used for testing cross-crate.

#![crate_type = "rlib"]
#![feature(type_alias_impl_trait)]

pub type Foo = impl std::fmt::Debug;

pub fn foo() -> Foo {
    5
}


