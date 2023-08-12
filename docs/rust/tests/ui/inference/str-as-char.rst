tests/ui/inference/str-as-char.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // When a char literal is used where a str should be,
// suggest changing to double quotes.

// run-rustfix

fn main() {
    let _: &str = 'a';   //~ ERROR mismatched types
    let _: &str = '"""'; //~ ERROR character literal may only contain one codepoint
    let _: &str = '\"\"\"'; //~ ERROR character literal may only contain one codepoint
}


