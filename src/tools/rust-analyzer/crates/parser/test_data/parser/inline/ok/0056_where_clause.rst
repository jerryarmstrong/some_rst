src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0056_where_clause.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo()
where
   'a: 'b + 'c,
   T: Clone + Copy + 'static,
   Iterator::Item: 'a,
   <T as Iterator>::Item: 'a
{}


