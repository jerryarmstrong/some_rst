src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0074_stmt_postfix_expr_ambiguity.rs
====================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        _ => {}
        () => {}
        [] => {}
    }
}


