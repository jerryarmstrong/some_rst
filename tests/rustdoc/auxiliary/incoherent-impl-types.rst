tests/rustdoc/auxiliary/incoherent-impl-types.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_has_incoherent_inherent_impls]
pub trait FooTrait {}

#[rustc_has_incoherent_inherent_impls]
pub struct FooStruct;


