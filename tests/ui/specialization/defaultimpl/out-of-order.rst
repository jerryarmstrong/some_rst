tests/ui/specialization/defaultimpl/out-of-order.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Test that you can list the more specific impl before the more general one.

#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

trait Foo {
    type Out;
}

impl Foo for bool {
    type Out = ();
}

default impl<T> Foo for T {
    type Out = bool;
}

fn main() {}


