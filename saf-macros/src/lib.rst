saf-macros/src/lib.rs
=====================

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    use crate::error::derive_error;
use proc_macro::TokenStream;

extern crate proc_macro;
mod error;

#[proc_macro_derive(ProgramErrorCode)]
pub fn derive_error_codes(input: TokenStream) -> TokenStream {
    derive_error(input)
}




