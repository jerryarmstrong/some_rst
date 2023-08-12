tests/ui/proc-macro/auxiliary/derive-atob.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(AToB)]
pub fn derive(input: TokenStream) -> TokenStream {
    let input = input.to_string();
    assert_eq!(input, "struct A ;");
    "struct B;".parse().unwrap()
}


