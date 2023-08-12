tests/ui/specialization/min_specialization/impl_specialization_trait.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that specialization traits can't be implemented without a feature.

// gate-test-min_specialization

// aux-build:specialization-trait.rs

extern crate specialization_trait;

struct A {}

impl specialization_trait::SpecTrait for A {
    //~^ ERROR implementing `rustc_specialization_trait` traits is unstable
    fn method(&self) {}
}

fn main() {}


