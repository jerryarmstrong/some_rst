tests/ui/half-open-range-patterns/slice_pattern_syntax_problem1.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Instead of allowing the previous case, maintain the feature gate for slice patterns for now.
fn main() {
    let xs = [13, 1, 5, 2, 3, 1, 21, 8];
    let [a @ 3.., b @ ..3, c @ 4..6, ..] = xs;
    //~^ `X..` patterns in slices are experimental
    //~| exclusive range pattern syntax is experimental
    //~| exclusive range pattern syntax is experimental
}


