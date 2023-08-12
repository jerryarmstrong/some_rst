tests/ui/specialization/min_specialization/specialization_trait.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `rustc_specialization_trait` requires always applicable impls.

#![feature(min_specialization)]
#![feature(rustc_attrs)]

#[rustc_specialization_trait]
trait SpecMarker {
    fn f();
}

impl SpecMarker for &'static u8 {
    //~^ ERROR cannot specialize
    fn f() {}
}

impl<T> SpecMarker for (T, T) {
    //~^ ERROR specializing impl
    fn f() {}
}

impl<T: Clone> SpecMarker for [T] {
    //~^ ERROR cannot specialize
    fn f() {}
}

fn main() {}


