tests/ui/range/range_traits-1.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::*;

#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
struct AllTheRanges {
    a: Range<usize>,
    //~^ ERROR can't compare
    //~| ERROR Ord
    b: RangeTo<usize>,
    //~^ ERROR can't compare
    //~| ERROR Ord
    c: RangeFrom<usize>,
    //~^ ERROR can't compare
    //~| ERROR Ord
    d: RangeFull,
    //~^ ERROR can't compare
    //~| ERROR Ord
    e: RangeInclusive<usize>,
    //~^ ERROR can't compare
    //~| ERROR Ord
    f: RangeToInclusive<usize>,
    //~^ ERROR can't compare
    //~| ERROR Ord
}

fn main() {}


