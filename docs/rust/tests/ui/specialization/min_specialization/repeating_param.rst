tests/ui/specialization/min_specialization/repeating_param.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that specializing on two type parameters being equal is not allowed.

#![feature(min_specialization)]

trait X {
    fn f();
}

impl<T> X for T {
    default fn f() {}
}
impl<T> X for (T, T) {
    //~^ ERROR specializing impl repeats parameter `T`
    fn f() {}
}

fn main() {}


