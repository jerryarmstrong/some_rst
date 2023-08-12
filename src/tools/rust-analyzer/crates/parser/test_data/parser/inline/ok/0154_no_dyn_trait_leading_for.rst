src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0154_no_dyn_trait_leading_for.rs
=================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = for<'a> Test<'a> + Send;


