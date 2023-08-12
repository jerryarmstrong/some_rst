tests/ui/specialization/min_specialization/specialize_on_trait.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that specializing on a trait is not allowed in general.

#![feature(min_specialization)]

trait SpecMarker {}

trait X {
    fn f();
}

impl<T> X for T {
    default fn f() {}
}

impl<T: SpecMarker> X for T {
    //~^ ERROR cannot specialize on trait `SpecMarker`
    fn f() {}
}

fn main() {}


