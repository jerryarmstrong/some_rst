src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0052_for_range_block.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
   for _x in 0 .. (0 .. {1 + 2}).sum::<u32>() {
       break;
   }
}


