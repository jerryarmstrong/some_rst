src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0177_trait_alias_where_clause.rs
=================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Z<U> = T<U> where U: Copy;
trait Z<U> = where Self: T<U>;


