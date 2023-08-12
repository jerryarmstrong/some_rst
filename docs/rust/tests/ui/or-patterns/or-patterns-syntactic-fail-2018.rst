tests/ui/or-patterns/or-patterns-syntactic-fail-2018.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that :pat doesn't accept top-level or-patterns in edition 2018.

// edition:2018

fn main() {}

// Test the `pat` macro fragment parser:
macro_rules! accept_pat {
    ($p:pat) => {};
}

accept_pat!(p | q); //~ ERROR no rules expected the token `|`
accept_pat!(|p| q); //~ ERROR no rules expected the token `|`


