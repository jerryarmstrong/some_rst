tests/ui/half-open-range-patterns/exclusive_range_pattern_syntax_collision.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(half_open_range_patterns_in_slices)]
#![feature(exclusive_range_pattern)]

fn main() {
    match [5..4, 99..105, 43..44] {
        [_, 99.., _] => {},
        //~^ ERROR mismatched types
        _ => {},
    }
}


