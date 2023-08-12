tests/ui/proc-macro/auxiliary/derive-b.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(B, attributes(B))]
pub fn derive_b(input: TokenStream) -> TokenStream {
    "".parse().unwrap()
}


