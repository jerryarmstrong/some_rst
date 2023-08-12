tests/ui/specialization/min_specialization/specialize_on_spec_trait.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that specializing on a `rustc_specialization_trait` trait is allowed.

// check-pass

#![feature(min_specialization)]
#![feature(rustc_attrs)]

#[rustc_specialization_trait]
trait SpecTrait {
    fn g(&self);
}

trait X {
    fn f(&self);
}

impl<T> X for T {
    default fn f(&self) {}
}

impl<T: SpecTrait> X for T {
    fn f(&self) {
        self.g();
    }
}

fn main() {}


