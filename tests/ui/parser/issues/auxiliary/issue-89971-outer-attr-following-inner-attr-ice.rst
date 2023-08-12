tests/ui/parser/issues/auxiliary/issue-89971-outer-attr-following-inner-attr-ice.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(ICE)]
pub fn derive(_: TokenStream) -> TokenStream {
    r#"#[allow(missing_docs)] struct X { }"#.parse().unwrap()
}


