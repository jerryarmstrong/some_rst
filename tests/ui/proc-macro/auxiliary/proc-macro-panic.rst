tests/ui/proc-macro/auxiliary/proc-macro-panic.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::{TokenStream, Ident, Span};

#[proc_macro]
pub fn panic_in_libproc_macro(_: TokenStream) -> TokenStream {
    Ident::new("", Span::call_site());
    TokenStream::new()
}


