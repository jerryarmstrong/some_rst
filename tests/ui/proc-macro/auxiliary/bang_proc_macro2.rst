tests/ui/proc-macro/auxiliary/bang_proc_macro2.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro]
pub fn bang_proc_macro2(_: TokenStream) -> TokenStream {
    "let x = foobar2;".parse().unwrap()
}


