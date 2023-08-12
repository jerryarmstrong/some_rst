tests/ui/proc-macro/auxiliary/custom-attr-only-one-derive.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(Foo)]
pub fn foo(a: TokenStream) -> TokenStream {
    "".parse().unwrap()
}

#[proc_macro_derive(Bar, attributes(custom))]
pub fn bar(a: TokenStream) -> TokenStream {
    "".parse().unwrap()
}


