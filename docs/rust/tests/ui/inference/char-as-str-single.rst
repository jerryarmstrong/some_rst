tests/ui/inference/char-as-str-single.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // When a SINGLE-character string literal is used where a char should be,
// suggest changing to single quotes.

// Testing both single-byte and multi-byte characters, as we should handle both.

// run-rustfix

fn main() {
    let _: char = "a"; //~ ERROR mismatched types
    let _: char = "人"; //~ ERROR mismatched types
    let _: char = "'"; //~ ERROR mismatched types
}


