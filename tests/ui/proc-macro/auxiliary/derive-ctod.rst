tests/ui/proc-macro/auxiliary/derive-ctod.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(CToD)]
pub fn derive(input: TokenStream) -> TokenStream {
    let input = input.to_string();
    assert_eq!(input, "struct C ;");
    "struct D;".parse().unwrap()
}


