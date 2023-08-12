src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0187_assoc_type_eq.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type T = StreamingIterator<Item<'a> = &'a T>;


