src/tools/clippy/tests/ui/len_zero_ranges.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::len_zero)]
#![allow(unused)]

// Now that `Range(Inclusive)::is_empty` is stable (1.47), we can always suggest this
mod issue_3807 {
    fn suggestion_is_fine_range() {
        let _ = (0..42).len() == 0;
    }

    fn suggestion_is_fine_range_inclusive() {
        let _ = (0_u8..=42).len() == 0;
    }
}

fn main() {}


