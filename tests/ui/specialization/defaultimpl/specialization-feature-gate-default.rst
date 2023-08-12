tests/ui/specialization/defaultimpl/specialization-feature-gate-default.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that specialization must be ungated to use the `default` keyword

trait Foo {
    fn foo(&self);
}

default impl<T> Foo for T { //~ ERROR specialization is unstable
    fn foo(&self) {}
}

fn main() {}


