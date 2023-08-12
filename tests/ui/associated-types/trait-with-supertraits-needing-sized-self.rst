tests/ui/associated-types/trait-with-supertraits-needing-sized-self.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::{Add, Sub, Mul, Div};

trait ArithmeticOps: Add<Output=Self> + Sub<Output=Self> + Mul<Output=Self> + Div<Output=Self> {}
//~^ ERROR the size for values of type `Self` cannot be known at compilation time

impl<T> ArithmeticOps for T where T: Add<Output=T> + Sub<Output=T> + Mul<Output=T> + Div<Output=T> {
    // Nothing to implement, since T already supports the other traits.
    // It has the functions it needs already
}

fn main() {}


