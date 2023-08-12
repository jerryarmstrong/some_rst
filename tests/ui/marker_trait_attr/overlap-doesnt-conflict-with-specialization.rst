tests/ui/marker_trait_attr/overlap-doesnt-conflict-with-specialization.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(marker_trait_attr)]
#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

#[marker]
trait MyMarker {}

impl<T> MyMarker for T {}
impl<T> MyMarker for Vec<T> {}

fn foo<T: MyMarker>(t: T) -> T {
    t
}

fn main() {
    assert_eq!(1, foo(1));
    assert_eq!(2.0, foo(2.0));
    assert_eq!(vec![1], foo(vec![1]));
}


