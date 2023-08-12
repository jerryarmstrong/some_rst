tests/ui/resolve/token-error-correct-2.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we do some basic error correction in the tokeniser (and don't ICE).

fn main() {
    if foo {
    //~^ ERROR: cannot find value `foo`
    ) //~ ERROR: mismatched closing delimiter: `)`
}


