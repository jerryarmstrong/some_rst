tests/ui/macros/auxiliary/dollar-crate-nested-encoding.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub type S = u8;

macro_rules! generate_exported { () => {
    #[macro_export]
    macro_rules! exported {
        () => ($crate::S)
    }
}}

generate_exported!();


