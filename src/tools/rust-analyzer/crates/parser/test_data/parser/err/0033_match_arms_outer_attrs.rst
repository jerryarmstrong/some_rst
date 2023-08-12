src/tools/rust-analyzer/crates/parser/test_data/parser/err/0033_match_arms_outer_attrs.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        _ => (),
        _ => (),
        #[cfg(test)]
    }
}


