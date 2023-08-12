src/tools/miri/tests/pass/stacked-borrows/zst-field-retagging-terminates.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-retag-fields
// Checks that the test does not run forever (which relies on a fast path).
fn main() {
    let array = [(); usize::MAX];
    drop(array); // Pass the array to a function, retagging its fields
}


