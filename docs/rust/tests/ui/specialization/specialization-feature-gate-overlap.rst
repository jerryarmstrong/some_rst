tests/ui/specialization/specialization-feature-gate-overlap.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that writing an overlapping impl is not allow unless specialization is ungated.

// gate-test-specialization

trait Foo {
    fn foo(&self);
}

impl<T> Foo for T {
    fn foo(&self) {}
}

impl Foo for u8 { //~ ERROR E0119
    fn foo(&self) {}
}

fn main() {}


