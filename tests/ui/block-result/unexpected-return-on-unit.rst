tests/ui/block-result/unexpected-return-on-unit.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we do some basic error correction in the tokeniser (and don't spew
// too many bogus errors).

fn foo() -> usize {
    3
}

fn bar() {
    foo() //~ ERROR mismatched types
}

fn main() {
    bar()
}


