src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0126_attr_on_expr_stmt.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    #[A] foo();
    #[B] bar!{}
    #[C] #[D] {}
    #[D] return ();
}


