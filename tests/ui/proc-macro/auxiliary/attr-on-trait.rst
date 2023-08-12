tests/ui/proc-macro/auxiliary/attr-on-trait.rs
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
pub fn foo(attr: TokenStream, item: TokenStream) -> TokenStream {
    drop(attr);
    assert_eq!(item.to_string(), "fn foo() {}");
    "fn foo(&self);".parse().unwrap()
}


