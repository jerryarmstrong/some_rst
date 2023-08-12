tests/ui/proc-macro/auxiliary/amputate-span.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_attribute]
pub fn drop_first_token(attr: TokenStream, input: TokenStream) -> TokenStream {
    assert!(attr.is_empty());
    input.into_iter().skip(1).collect()
}


