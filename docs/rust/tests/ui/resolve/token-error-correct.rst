tests/ui/resolve/token-error-correct.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we do some basic error correction in the tokeniser.

fn main() {
    foo(bar(;
    //~^ ERROR cannot find function `bar` in this scope
}
//~^ ERROR: mismatched closing delimiter: `}`

fn foo(_: usize) {}


