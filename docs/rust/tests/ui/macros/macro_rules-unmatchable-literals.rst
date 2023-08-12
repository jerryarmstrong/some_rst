tests/ui/macros/macro_rules-unmatchable-literals.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Pinning tests for things that don't work to make sure we notice if that changes

#![crate_type = "lib"]

macro_rules! octal_with_bad_digit {
    ( 0o1238 ) => {}; //~ ERROR invalid digit
}

macro_rules! binary_with_bad_digit {
    ( 0b012 ) => {}; //~ ERROR invalid digit
}

// This can't happen for Hex and Decimal as things like `123A` and `0xFFG`
// get treated as unknown *suffixes*, rather than digits.


