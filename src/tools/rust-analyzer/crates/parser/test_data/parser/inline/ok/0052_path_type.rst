src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0052_path_type.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = Foo;
type B = ::Foo;
type C = self::Foo;
type D = super::Foo;


