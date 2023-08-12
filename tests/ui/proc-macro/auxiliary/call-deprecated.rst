tests/ui/proc-macro/auxiliary/call-deprecated.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro_attribute]
#[deprecated(since = "1.0.0", note = "test")]
pub fn attr(_: TokenStream, input: TokenStream) -> TokenStream {
    input
}

#[proc_macro_attribute]
#[deprecated(since = "1.0.0", note = "test")]
pub fn attr_remove(_: TokenStream, _: TokenStream) -> TokenStream {
    TokenStream::new()
}


