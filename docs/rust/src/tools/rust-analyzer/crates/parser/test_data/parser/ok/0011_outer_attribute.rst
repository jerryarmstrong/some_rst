src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0011_outer_attribute.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(test)]
#[Ignore]
fn foo() {}

#[path = "a.rs"]
mod b;


