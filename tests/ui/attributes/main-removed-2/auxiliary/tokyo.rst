tests/ui/attributes/main-removed-2/auxiliary/tokyo.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::TokenStream;

#[proc_macro_attribute]
pub fn main(_: TokenStream, input: TokenStream) -> TokenStream {
    "fn main() { println!(\"Hello Tokyo!\"); }".parse().unwrap()
}


