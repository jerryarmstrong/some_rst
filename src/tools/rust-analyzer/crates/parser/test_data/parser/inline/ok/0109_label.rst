src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0109_label.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    'a: loop {}
    'b: while true {}
    'c: for x in () {}
}


