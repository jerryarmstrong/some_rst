tests/ui/pattern/move-ref-patterns/move-ref-patterns-default-binding-modes-fixable.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(unused_variables)]
fn main() {
    struct U;

    // A tuple is a "non-reference pattern".
    // A `mut` binding pattern resets the binding mode to by-value.

    let mut p = (U, U);
    let (a, mut b) = &mut p;
    //~^ ERROR cannot move out of a mutable reference
}


