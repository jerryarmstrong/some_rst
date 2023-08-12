lang/attribute/constant/src/lib.rs
==================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    extern crate proc_macro;

/// A marker attribute used to mark const values that should be included in the
/// generated IDL but functionally does nothing.
#[proc_macro_attribute]
pub fn constant(
    _attr: proc_macro::TokenStream,
    input: proc_macro::TokenStream,
) -> proc_macro::TokenStream {
    input
}


