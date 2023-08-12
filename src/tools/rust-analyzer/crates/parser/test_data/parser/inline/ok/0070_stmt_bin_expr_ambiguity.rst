src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0070_stmt_bin_expr_ambiguity.rs
================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() {
    let _ = {1} & 2;
    {1} &2;
}


