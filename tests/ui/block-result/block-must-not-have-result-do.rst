tests/ui/block-result/block-must-not-have-result-do.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    loop {
        true //~  ERROR mismatched types
    }
}


