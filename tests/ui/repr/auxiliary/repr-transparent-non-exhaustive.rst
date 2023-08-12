tests/ui/repr/auxiliary/repr-transparent-non-exhaustive.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

pub struct Private { _priv: () }

#[non_exhaustive]
pub struct NonExhaustive {}

#[non_exhaustive]
pub enum NonExhaustiveEnum {}

pub enum NonExhaustiveVariant {
    #[non_exhaustive]
    A,
}

pub struct ExternalIndirection<T> {
    pub x: T,
}


