tests/ui/attributes/auxiliary/key-value-expansion.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro_derive(EthabiContract, attributes(ethabi_contract_options))]
pub fn ethabi_derive(input: TokenStream) -> TokenStream {
    Default::default()
}


