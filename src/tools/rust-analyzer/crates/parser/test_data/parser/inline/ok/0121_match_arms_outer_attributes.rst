src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0121_match_arms_outer_attributes.rs
====================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        #[cfg(feature = "some")]
        _ => (),
        #[cfg(feature = "other")]
        _ => (),
        #[cfg(feature = "many")]
        #[cfg(feature = "attributes")]
        #[cfg(feature = "before")]
        _ => (),
    }
}


