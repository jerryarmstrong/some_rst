src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0201_question_for_type_trait_bound.rs
======================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<T>() where T: ?for<> Sized {}


