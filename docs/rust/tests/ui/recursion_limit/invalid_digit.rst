tests/ui/recursion_limit/invalid_digit.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the parse error for an invalid digit in recursion_limit

#![recursion_limit = "-100"] //~ ERROR `limit` must be a non-negative integer
                             //~| not a valid integer
                             //~| ERROR `limit` must be a non-negative integer
                             //~| not a valid integer
fn main() {}


