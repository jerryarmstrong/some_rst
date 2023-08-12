tests/ui/specialization/min_specialization/spec-iter.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we can specialize on a concrete iterator type. This requires us
// to consider which parameters in the parent impl are constrained.

// check-pass

#![feature(min_specialization)]

trait SpecFromIter<T> {
    fn f(&self);
}

impl<'a, T: 'a, I: Iterator<Item = &'a T>> SpecFromIter<T> for I {
    default fn f(&self) {}
}

impl<'a, T> SpecFromIter<T> for std::slice::Iter<'a, T> {
    fn f(&self) {}
}

fn main() {}


