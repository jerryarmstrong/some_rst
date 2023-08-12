tests/ui/cross-crate/auxiliary/xcrate_associated_type_defaults.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_type_defaults)]

pub trait Foo<T: Default + ToString> {
    type Out: Default + ToString = T;
}

impl Foo<u32> for () {
}

impl Foo<u64> for () {
    type Out = bool;
}


