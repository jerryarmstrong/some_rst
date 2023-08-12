src/tools/rust-analyzer/crates/parser/test_data/parser/err/0023_mismatched_paren.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    foo! (
        bar, "baz", 1, 2.0
    } //~ ERROR incorrect close delimiter
}


