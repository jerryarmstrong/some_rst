tests/ui/nll/ty-outlives/impl-trait-captures.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Zverbose

#![allow(warnings)]

trait Foo<'a> {
}

impl<'a, T> Foo<'a> for T { }

fn foo<'a, T>(x: &T) -> impl Foo<'a> {
    x
    //~^ ERROR captures lifetime that does not appear in bounds
}

fn main() {}


