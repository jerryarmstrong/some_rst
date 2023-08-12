src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0029_range_forms.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    ..1 + 1;
    ..z = 2;
    x = false..1 == 1;
    let x = 1..;
    
    ..=1 + 1;
    ..=z = 2;
    x = false..=1 == 1;
    let x = 1..;
}


