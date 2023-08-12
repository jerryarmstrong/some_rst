tests/ui/associated-types/associated-types-projection-bound-in-supertraits.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// Test that we correctly handle projection bounds appearing in the
// supertrait list (and in conjunction with overloaded operators). In
// this case, the `Result=Self` binding in the supertrait listing of
// `Int` was being ignored.

trait Not {
    type Result;

    fn not(self) -> Self::Result;
}

trait Int: Not<Result=Self> + Sized {
    fn count_ones(self) -> usize;
    fn count_zeros(self) -> usize {
        // neither works
        let x: Self = self.not();
        0
    }
}

fn main() { }


