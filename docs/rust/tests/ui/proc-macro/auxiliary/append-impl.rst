tests/ui/proc-macro/auxiliary/append-impl.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(Append)]
pub fn derive_a(input: TokenStream) -> TokenStream {
    "impl Append for A {
         fn foo(&self) {}
     }
    ".parse().unwrap()
}


