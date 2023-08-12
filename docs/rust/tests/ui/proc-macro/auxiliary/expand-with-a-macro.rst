tests/ui/proc-macro/auxiliary/expand-with-a-macro.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]
#![deny(warnings)]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(A)]
pub fn derive(input: TokenStream) -> TokenStream {
    let input = input.to_string();
    assert!(input.contains("struct A ;"));
    r#"
        impl A {
            fn a(&self) {
                panic!("hello");
            }
        }
    "#.parse().unwrap()
}


