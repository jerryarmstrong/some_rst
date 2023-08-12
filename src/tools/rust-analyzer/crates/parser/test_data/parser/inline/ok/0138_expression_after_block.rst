src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0138_expression_after_block.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
   let mut p = F{x: 5};
   {p}.x = 10;
}


