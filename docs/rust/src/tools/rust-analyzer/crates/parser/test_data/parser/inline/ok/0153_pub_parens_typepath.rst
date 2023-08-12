src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0153_pub_parens_typepath.rs
============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct B(pub (super::A));
struct B(pub (crate::A,));


