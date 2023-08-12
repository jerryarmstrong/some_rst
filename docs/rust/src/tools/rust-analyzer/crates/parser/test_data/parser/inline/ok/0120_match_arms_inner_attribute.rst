src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0120_match_arms_inner_attribute.rs
===================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        #![doc("Inner attribute")]
        #![doc("Can be")]
        #![doc("Stacked")]
        _ => (),
    }
}


