tests/ui/specialization/min_specialization/repeated_projection_type.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that projection bounds can't be specialized on.

#![feature(min_specialization)]

trait X {
    fn f();
}
trait Id {
    type This;
}
impl<T> Id for T {
    type This = T;
}

impl<T: Id> X for T {
    default fn f() {}
}

impl<I, V: Id<This = (I,)>> X for V {
    //~^ ERROR cannot specialize on
    fn f() {}
}

fn main() {}


