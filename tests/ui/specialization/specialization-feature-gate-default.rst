tests/ui/specialization/specialization-feature-gate-default.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that specialization must be ungated to use the `default` keyword

// gate-test-specialization

trait Foo {
    fn foo(&self);
}

impl<T> Foo for T {
    default fn foo(&self) {} //~ ERROR specialization is unstable
}

fn main() {}


