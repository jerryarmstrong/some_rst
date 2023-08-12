src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0137_await_expr.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    x.await;
    x.0.await;
    x.0().await?.hello();
}


