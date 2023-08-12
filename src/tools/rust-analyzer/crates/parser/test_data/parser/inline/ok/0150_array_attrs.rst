src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0150_array_attrs.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const A: &[i64] = &[1, #[cfg(test)] 2];


