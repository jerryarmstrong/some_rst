src/tools/rust-analyzer/crates/parser/test_data/parser/err/0013_invalid_type.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Cache(
    RefCell<HashMap<
        TypeId,
        Box<@ Any>,
    >>
);



