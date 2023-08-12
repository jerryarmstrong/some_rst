tests/ui/half-open-range-patterns/pat-tuple-4.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(exclusive_range_pattern)]

fn main() {
    const PAT: u8 = 1;

    match 0 {
        (.. PAT) => {}
        _ => {}
    }
}


