src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0058_unary_expr_precedence.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    1 + *&2 + 3;
    *&1 as u64;
    *x(1);
    &x[1];
    -1..2;
}


