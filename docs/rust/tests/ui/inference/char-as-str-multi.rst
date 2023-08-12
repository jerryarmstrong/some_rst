tests/ui/inference/char-as-str-multi.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // When a MULTI/NO-character string literal is used where a char should be,
// DO NOT suggest changing to single quotes.

fn main() {
    let _: char = "foo"; //~ ERROR mismatched types
    let _: char = ""; //~ ERROR mismatched types
}


