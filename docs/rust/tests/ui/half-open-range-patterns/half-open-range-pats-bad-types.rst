tests/ui/half-open-range-patterns/half-open-range-pats-bad-types.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(exclusive_range_pattern)]

fn main() {
    let "a".. = "a"; //~ ERROR only `char` and numeric types are allowed in range patterns
    let .."a" = "a"; //~ ERROR only `char` and numeric types are allowed in range patterns
    let ..="a" = "a"; //~ ERROR only `char` and numeric types are allowed in range patterns
}


