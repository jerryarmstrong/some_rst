tests/ui/half-open-range-patterns/feature-gate-half-open-range-patterns-in-slices.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(exclusive_range_pattern)]

fn main() {
    let xs = [13, 1, 5, 2, 3, 1, 21, 8];
    let [a @ 3.., b @ ..3, c @ 4..6, ..] = xs;
    //~^ `X..` patterns in slices are experimental
}


