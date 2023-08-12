tests/ui/proc-macro/auxiliary/derive-two-attrs.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::*;

#[proc_macro_derive(A, attributes(b))]
pub fn foo(_x: TokenStream) -> TokenStream {
    TokenStream::new()
}


