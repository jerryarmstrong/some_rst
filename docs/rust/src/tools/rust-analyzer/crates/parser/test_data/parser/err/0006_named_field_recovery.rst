src/tools/rust-analyzer/crates/parser/test_data/parser/err/0006_named_field_recovery.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    f: u32,
    pub 92
    + - *
    pub x: u32,
    z: f64,
}


