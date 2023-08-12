tests/ui/type-alias-impl-trait/unused_generic_param.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
#![allow(dead_code)]

fn main() {}

type PartiallyDefined<T> = impl Sized;

fn partially_defined<T: std::fmt::Debug>(_: T) -> PartiallyDefined<T> {
    4u32
}

type PartiallyDefined2<T> = impl Sized;

fn partially_defined2<T: std::fmt::Debug>(_: T) -> PartiallyDefined2<T> {
    4u32
}

fn partially_defined22<T>(_: T) -> PartiallyDefined2<T> {
    4u32
}


