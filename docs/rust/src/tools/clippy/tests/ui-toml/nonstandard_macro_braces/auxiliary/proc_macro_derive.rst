src/tools/clippy/tests/ui-toml/nonstandard_macro_braces/auxiliary/proc_macro_derive.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit=link
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(DeriveSomething)]
pub fn derive(_: TokenStream) -> TokenStream {
    "fn _f() -> Vec<u8> { vec![] }".parse().unwrap()
}

#[proc_macro]
pub fn foo_bar(_: TokenStream) -> TokenStream {
    "fn issue_7422() { eprintln!(); }".parse().unwrap()
}


