src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0160_crate_visibility_in.rs
============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub(in super::A) struct S;
pub(in crate) struct S;


