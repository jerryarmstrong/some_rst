src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0061_record_lit.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    S {};
    S { x };
    S { x, y: 32, };
    S { x, y: 32, ..Default::default() };
    S { x: ::default() };
    TupleStruct { 0: 1 };
}


