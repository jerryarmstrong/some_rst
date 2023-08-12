src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0029_cast_expr.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    82 as i32;
    81 as i8 + 1;
    79 as i16 - 1;
    0x36 as u8 <= 0x37;
}


