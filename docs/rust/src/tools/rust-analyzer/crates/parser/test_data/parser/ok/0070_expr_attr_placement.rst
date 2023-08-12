src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0070_expr_attr_placement.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() {
    (#[a] lhs? + #[b] rhs.await)
}


