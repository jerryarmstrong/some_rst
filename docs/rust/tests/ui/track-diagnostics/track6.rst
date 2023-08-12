tests/ui/track-diagnostics/track6.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z track-diagnostics
// error-pattern: created at



pub trait Foo {
    fn bar();
}

impl <T> Foo for T {
    default fn bar() {}
}

fn main() {}


