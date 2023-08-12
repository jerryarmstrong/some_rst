tests/rustdoc/auxiliary/masked.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
pub struct MaskedStruct;

pub trait MaskedTrait {
    fn masked_method();
}

impl MaskedTrait for String {
    fn masked_method() {}
}

pub trait MaskedBlanketTrait {}

impl<T> MaskedBlanketTrait for T {}


