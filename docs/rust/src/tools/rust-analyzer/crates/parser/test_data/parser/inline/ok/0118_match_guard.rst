src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0118_match_guard.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        _ if foo => (),
        _ if let foo = bar => (),
    }
}


