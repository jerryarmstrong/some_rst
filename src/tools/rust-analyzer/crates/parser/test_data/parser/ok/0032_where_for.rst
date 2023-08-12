src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0032_where_for.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test_serialization<SER>()
where
    SER: Serialize + for<'de> Deserialize<'de> + PartialEq + std::fmt::Debug,
{}


