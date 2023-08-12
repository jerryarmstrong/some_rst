src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0125_record_literal_field_with_attr.rs
=======================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    S { #[cfg(test)] field: 1 }
}


