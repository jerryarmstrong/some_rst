src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0132_box_expr.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let x = box 1i32;
    let y = (box 1i32, box 2i32);
    let z = Foo(box 1i32, box 2i32);
}


