src/tools/rust-analyzer/crates/parser/test_data/parser/err/0005_attribute_recover.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[foo(foo, +, 92)]
fn foo() {
}


#[foo(
fn foo() {
}


