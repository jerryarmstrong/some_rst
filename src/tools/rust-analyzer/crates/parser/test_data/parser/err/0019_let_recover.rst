src/tools/rust-analyzer/crates/parser/test_data/parser/err/0019_let_recover.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let foo = 11
    let bar = 1;
    let
    let baz = 92;
    let
    if true {}
    let
    while true {}
    let
    loop {}
}


