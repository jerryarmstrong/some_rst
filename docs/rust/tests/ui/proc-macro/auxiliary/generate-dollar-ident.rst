tests/ui/proc-macro/auxiliary/generate-dollar-ident.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![feature(proc_macro_quote)]
#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro]
pub fn dollar_ident(input: TokenStream) -> TokenStream {
    let black_hole = input.into_iter().next().unwrap();
    quote! {
        $black_hole!($$var);
    }
}


