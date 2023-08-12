tests/ui/specialization/min_specialization/repeating_lifetimes.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that directly specializing on repeated lifetime parameters is not
// allowed.

#![feature(min_specialization)]

trait X {
    fn f();
}

impl<T> X for T {
    default fn f() {}
}

impl<'a> X for (&'a u8, &'a u8) {
    //~^ ERROR specializing impl repeats parameter `'a`
    fn f() {}
}

fn main() {}


