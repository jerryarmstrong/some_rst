src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0034_break_expr.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    loop {
        break;
        break 'l;
        break 92;
        break 'l 92;
    }
}


