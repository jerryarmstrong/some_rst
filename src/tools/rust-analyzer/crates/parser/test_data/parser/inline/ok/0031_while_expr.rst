src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0031_while_expr.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    while true {};
    while let Some(x) = it.next() {};
    while { true } {};
}


