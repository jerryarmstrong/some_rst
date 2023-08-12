src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0024_slice_pat.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let [a, b, ..] = [];
    let [| a, ..] = [];
}


