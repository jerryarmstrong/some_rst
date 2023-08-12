tests/ui/rfc-2565-param-attrs/auxiliary/ident-mac.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_attribute]
pub fn id(_: TokenStream, input: TokenStream) -> TokenStream { input }


