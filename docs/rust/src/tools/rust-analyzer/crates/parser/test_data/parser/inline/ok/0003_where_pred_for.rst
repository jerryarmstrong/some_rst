src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0003_where_pred_for.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn for_trait<F>()
where
   for<'a> F: Fn(&'a str)
{ }


