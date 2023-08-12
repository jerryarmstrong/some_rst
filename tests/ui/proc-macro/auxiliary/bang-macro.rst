tests/ui/proc-macro/auxiliary/bang-macro.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro]
pub fn rewrite(input: TokenStream) -> TokenStream {
    let input = input.to_string();

    assert_eq!(input, r#""Hello, world!""#);

    r#""NOT Hello, world!""#.parse().unwrap()
}


