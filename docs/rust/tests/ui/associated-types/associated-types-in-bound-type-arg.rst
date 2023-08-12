tests/ui/associated-types/associated-types-in-bound-type-arg.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test the case where we resolve `C::Result` and the trait bound
// itself includes a `Self::Item` shorthand.
//
// Regression test for issue #33425.

trait ParallelIterator {
    type Item;
    fn drive_unindexed<C>(self, consumer: C) -> C::Result
        where C: Consumer<Self::Item>;
}

pub trait Consumer<ITEM> {
    type Result;
}

fn main() { }


