src/tools/rust-analyzer/crates/syntax/test_data/parser/validation/0038_endless_inclusive_range.rs
=================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    0..=;
    ..=;
}


