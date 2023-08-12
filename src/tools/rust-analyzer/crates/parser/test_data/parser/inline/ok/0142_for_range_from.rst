src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0142_for_range_from.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
   for x in 0 .. {
       break;
   }
}


