tests/ui/traits/bound/sugar.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests for "default" bounds inferred for traits with no bounds list.

trait Foo {}

fn a(_x: Box<dyn Foo + Send>) {
}

fn b(_x: &'static (dyn Foo + 'static)) {
}

fn c(x: Box<dyn Foo + Sync>) {
    a(x); //~ ERROR mismatched types
}

fn d(x: &'static (dyn Foo + Sync)) {
    b(x);
}

fn main() {}


