src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0042_call_expr.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let _ = f();
    let _ = f()(1)(1, 2,);
    let _ = f(<Foo>::func());
    f(<Foo as Trait>::func());
}


