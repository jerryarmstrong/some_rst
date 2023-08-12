src/tools/rust-analyzer/crates/parser/test_data/parser/inline/err/0014_record_literal_before_ellipsis_recovery.rs
=================================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    S { field ..S::default() }
}


