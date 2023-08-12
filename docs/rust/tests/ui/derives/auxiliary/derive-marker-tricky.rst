tests/ui/derives/auxiliary/derive-marker-tricky.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro_derive(NoMarker)]
pub fn f(input: TokenStream) -> TokenStream {
    if input.to_string().contains("rustc_copy_clone_marker") {
        panic!("found `#[rustc_copy_clone_marker]`");
    }
    TokenStream::new()
}


