tests/ui/rust-2018/auxiliary/suggestions-not-always-applicable.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::*;

#[proc_macro_attribute]
pub fn foo(_attr: TokenStream, _f: TokenStream) -> TokenStream {
    "pub fn foo() -> ::Foo { ::Foo }".parse().unwrap()
}


