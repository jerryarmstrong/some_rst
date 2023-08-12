tests/ui/specialization/min_specialization/implcit-well-formed-bounds.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that specializing on the well-formed predicates of the trait and
// self-type of an impl is allowed.

// check-pass

#![feature(min_specialization)]

struct OrdOnly<T: Ord>(T);

trait SpecTrait<U> {
    fn f();
}

impl<T, U> SpecTrait<U> for T {
    default fn f() {}
}

impl<T: Ord> SpecTrait<()> for OrdOnly<T> {
    fn f() {}
}

impl<T: Ord> SpecTrait<OrdOnly<T>> for () {
    fn f() {}
}

impl<T: Ord, U: Ord, V: Ord> SpecTrait<(OrdOnly<T>, OrdOnly<U>)> for &[OrdOnly<V>] {
    fn f() {}
}

fn main() {}


