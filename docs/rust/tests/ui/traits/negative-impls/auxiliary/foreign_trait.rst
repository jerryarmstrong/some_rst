tests/ui/traits/negative-impls/auxiliary/foreign_trait.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]
#![feature(with_negative_coherence)]

pub trait ForeignTrait {}

impl ForeignTrait for u32 {}
impl !ForeignTrait for String {}


