src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0064_if_expr.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    if true {};
    if true {} else {};
    if true {} else if false {} else {};
    if S {};
    if { true } { } else { };
}


