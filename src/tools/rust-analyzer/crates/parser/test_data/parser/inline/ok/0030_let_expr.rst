src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0030_let_expr.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    if let Some(_) = None && true {}
    while 1 == 5 && (let None = None) {}
}


