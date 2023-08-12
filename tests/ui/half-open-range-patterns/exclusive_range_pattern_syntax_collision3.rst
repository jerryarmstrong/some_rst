tests/ui/half-open-range-patterns/exclusive_range_pattern_syntax_collision3.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(exclusive_range_pattern)]

fn main() {
    match [5..4, 99..105, 43..44] {
        [..9, 99..100, _] => {},
        //~^ ERROR mismatched types
        //~| ERROR mismatched types
        //~| ERROR mismatched types
        _ => {},
    }
}


