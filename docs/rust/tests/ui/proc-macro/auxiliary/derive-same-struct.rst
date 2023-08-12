tests/ui/proc-macro/auxiliary/derive-same-struct.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(AToB)]
pub fn derive1(input: TokenStream) -> TokenStream {
    println!("input1: {:?}", input.to_string());
    assert_eq!(input.to_string(), "struct A ;");
    "#[derive(BToC)] struct B;".parse().unwrap()
}

#[proc_macro_derive(BToC)]
pub fn derive2(input: TokenStream) -> TokenStream {
    assert_eq!(input.to_string(), "struct B ;");
    "struct C;".parse().unwrap()
}


