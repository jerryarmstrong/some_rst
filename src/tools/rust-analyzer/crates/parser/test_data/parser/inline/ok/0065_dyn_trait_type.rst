src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0065_dyn_trait_type.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = dyn Iterator<Item=Foo<'a>> + 'a;


