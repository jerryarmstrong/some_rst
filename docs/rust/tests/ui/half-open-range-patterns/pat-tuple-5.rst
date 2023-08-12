tests/ui/half-open-range-patterns/pat-tuple-5.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(exclusive_range_pattern)]

fn main() {
    const PAT: u8 = 1;

    match (0, 1) {
        (PAT ..) => {} //~ ERROR mismatched types
    }
}


