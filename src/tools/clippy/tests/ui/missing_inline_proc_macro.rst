src/tools/clippy/tests/ui/missing_inline_proc_macro.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::missing_inline_in_public_items)]
#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

fn _foo() {}

#[proc_macro]
pub fn function_like(_: TokenStream) -> TokenStream {
    TokenStream::new()
}

#[proc_macro_attribute]
pub fn attribute(_: TokenStream, _: TokenStream) -> TokenStream {
    TokenStream::new()
}

#[proc_macro_derive(Derive)]
pub fn derive(_: TokenStream) -> TokenStream {
    TokenStream::new()
}


