src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0080_postfix_range.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let x = 1..;
    match 1.. { _ => () };
    match a.b()..S { _ => () };
}


