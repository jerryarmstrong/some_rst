src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0053_path_expr.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let _ = a;
    let _ = a::b;
    let _ = ::a::<b>;
    let _ = format!();
}


