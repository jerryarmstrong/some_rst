src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0158_macro_rules_non_brace.rs
==============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! m ( ($i:ident) => {} );
macro_rules! m [ ($i:ident) => {} ];


