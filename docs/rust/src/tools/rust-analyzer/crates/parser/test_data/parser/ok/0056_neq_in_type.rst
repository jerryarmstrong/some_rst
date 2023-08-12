src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0056_neq_in_type.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    if 1.0f32.floor() as i64 != 1.0f32.floor() as i64 {}
}


