src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0037_qual_paths.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type X = <A as B>::Output;
fn foo() { <usize as Default>::default(); }


