tests/ui/proc-macro/auxiliary/derive-union.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(UnionTest)]
pub fn derive(input: TokenStream) -> TokenStream {
    let input = input.to_string();
    assert!(input.contains("#[repr(C)]"));
    assert!(input.contains("union Test {"));
    assert!(input.contains("a : u8,"));
    assert!(input.contains("}"));
    "".parse().unwrap()
}


