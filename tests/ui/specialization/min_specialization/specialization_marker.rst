tests/ui/specialization/min_specialization/specialization_marker.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `rustc_unsafe_specialization_marker` is only allowed on marker traits.

#![feature(rustc_attrs)]

#[rustc_unsafe_specialization_marker]
trait SpecMarker {
    fn f();
    //~^ ERROR marker traits
}

#[rustc_unsafe_specialization_marker]
trait SpecMarker2 {
    type X;
    //~^ ERROR marker traits
}

fn main() {}


