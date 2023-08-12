tests/ui/block-result/block-must-not-have-result-while.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    while true { //~ WARN denote infinite loops with
        true //~  ERROR mismatched types
             //~| expected `()`, found `bool`
    }
}


