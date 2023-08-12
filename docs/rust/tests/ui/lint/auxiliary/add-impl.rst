tests/ui/lint/auxiliary/add-impl.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(AddImpl)]
// Unnecessary qualification `bar::foo`
// https://github.com/rust-lang/rust/issues/71898
pub fn derive(input: TokenStream) -> TokenStream {
    "impl B {
            fn foo(&self) { use bar::foo; bar::foo() }
        }

        fn foo() {}

        mod bar { pub fn foo() {} }
    ".parse().unwrap()
}


