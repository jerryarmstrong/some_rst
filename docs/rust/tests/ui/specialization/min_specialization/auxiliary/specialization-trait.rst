tests/ui/specialization/min_specialization/auxiliary/specialization-trait.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_specialization_trait]
pub trait SpecTrait {
    fn method(&self);
}


