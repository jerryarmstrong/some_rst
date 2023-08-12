tests/rustdoc/rustc-macro-crate.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic
// compile-flags: --crate-type proc-macro

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(Foo)]
pub fn foo(input: TokenStream) -> TokenStream {
    input
}


