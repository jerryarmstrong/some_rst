tests/ui/range/range-pattern-out-of-bounds-issue-68972.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(exclusive_range_pattern)]
#![allow(unreachable_patterns)]
fn main() {
    match 0u8 {
        251..257 => {}
        //~^ ERROR literal out of range
        //~| ERROR literal out of range
        251..=256 => {}
        //~^ ERROR literal out of range
        //~| ERROR literal out of range
        _ => {}
    }
}


