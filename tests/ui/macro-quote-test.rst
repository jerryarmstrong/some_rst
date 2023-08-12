tests/ui/macro-quote-test.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a macro can emit delimiters with nothing inside - `()`, `{}`

// run-pass
// aux-build:hello_macro.rs

extern crate hello_macro;

fn main() {
    hello_macro::hello!();
}


