src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0053_outer_attribute_on_macro_rules.rs
================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// Some docs
#[macro_export]
macro_rules! foo {
    () => {};
}


