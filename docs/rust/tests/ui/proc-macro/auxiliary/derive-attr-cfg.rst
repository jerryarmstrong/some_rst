tests/ui/proc-macro/auxiliary/derive-attr-cfg.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(Foo, attributes(foo))]
pub fn derive(input: TokenStream) -> TokenStream {
    assert!(!input.to_string().contains("#[cfg(any())]"));
    "".parse().unwrap()
}


