tests/ui/specialization/min_specialization/specialize_on_static.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that directly specializing on `'static` is not allowed.

#![feature(min_specialization)]

trait X {
    fn f();
}

impl<T> X for &'_ T {
    default fn f() {}
}

impl X for &'static u8 {
    //~^ ERROR cannot specialize on `'static` lifetime
    fn f() {}
}

fn main() {}


