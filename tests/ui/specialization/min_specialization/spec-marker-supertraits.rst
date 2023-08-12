tests/ui/specialization/min_specialization/spec-marker-supertraits.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that supertraits cannot be used to work around min_specialization
// limitations.

#![feature(min_specialization)]
#![feature(rustc_attrs)]

trait HasMethod {
    fn method(&self);
}

#[rustc_unsafe_specialization_marker]
trait Marker: HasMethod {}

trait Spec {
    fn spec_me(&self);
}

impl<T> Spec for T {
    default fn spec_me(&self) {}
}

impl<T: Marker> Spec for T {
    //~^ ERROR cannot specialize on trait `HasMethod`
    fn spec_me(&self) {
        self.method();
    }
}

fn main() {}


