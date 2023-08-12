tests/ui/parser/keyword-try-as-identifier-edition2018.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018

fn main() {
    let try = "foo"; //~ error: expected identifier, found reserved keyword `try`
}


