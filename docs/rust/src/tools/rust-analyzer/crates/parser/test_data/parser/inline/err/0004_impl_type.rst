src/tools/rust-analyzer/crates/parser/test_data/parser/inline/err/0004_impl_type.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl Type {}
impl Trait1 for T {}
impl impl NotType {}
impl Trait2 for impl NotType {}


