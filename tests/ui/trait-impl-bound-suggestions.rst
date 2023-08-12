tests/ui/trait-impl-bound-suggestions.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[allow(unused)]
use std::fmt::Debug;
// Rustfix should add this, or use `std::fmt::Debug` instead.

#[allow(dead_code)]
struct ConstrainedStruct<X: Copy> {
    x: X
}

#[allow(dead_code)]
trait InsufficientlyConstrainedGeneric<X=()> {
    fn return_the_constrained_type(&self, x: X) -> ConstrainedStruct<X> {
        //~^ ERROR the trait bound `X: Copy` is not satisfied
        ConstrainedStruct { x }
    }
}

pub fn main() { }


