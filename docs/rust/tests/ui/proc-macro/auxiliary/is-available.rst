tests/ui/proc-macro/auxiliary/is-available.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::{Literal, TokenStream, TokenTree};

#[proc_macro]
pub fn from_inside_proc_macro(_input: TokenStream) -> TokenStream {
    proc_macro::is_available().to_string().parse().unwrap()
}


