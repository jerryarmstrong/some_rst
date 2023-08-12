tests/ui/resolve/token-error-correct-4.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// Test that we do some basic error correction in the tokeniser and apply suggestions.

fn setsuna(_: ()) {}

fn kazusa() {}

fn main() {
    setsuna(kazusa(); //~ ERROR: expected one of
} //~ ERROR: expected expression


