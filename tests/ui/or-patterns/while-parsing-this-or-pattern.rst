tests/ui/or-patterns/while-parsing-this-or-pattern.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the parser for the "while parsing this or-pattern..." label here.

fn main() {
    match Some(42) {
        Some(42) | .=. => {} //~ ERROR expected pattern, found `.`
        //~^ while parsing this or-pattern starting here
        //~| NOTE expected pattern
    }
}


