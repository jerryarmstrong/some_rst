src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0059_match_arms_commas.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        _ => (),
        _ => {}
        _ => ()
    }
}


