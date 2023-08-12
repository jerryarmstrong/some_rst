tests/ui/specialization/min_specialization/spec-reference.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that lifetime parameters are allowed in specializing impls.

// check-pass

#![feature(min_specialization)]

trait MySpecTrait {
    fn f();
}

impl<T> MySpecTrait for T {
    default fn f() {}
}

impl<'a, T: ?Sized> MySpecTrait for &'a T {
    fn f() {}
}

fn main() {}


