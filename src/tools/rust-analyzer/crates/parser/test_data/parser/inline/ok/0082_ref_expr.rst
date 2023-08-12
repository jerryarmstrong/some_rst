src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0082_ref_expr.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    // reference operator
    let _ = &1;
    let _ = &mut &f();
    let _ = &raw;
    let _ = &raw.0;
    // raw reference operator
    let _ = &raw mut foo;
    let _ = &raw const foo;
}


