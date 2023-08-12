tests/ui/suggestions/auxiliary/proc-macro-type-error.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic
#![crate_type = "proc-macro"]
#![feature(proc_macro_quote)]

extern crate proc_macro;

use proc_macro::{quote, TokenStream};

#[proc_macro_attribute]
pub fn hello(_: TokenStream, _: TokenStream) -> TokenStream {
    quote!(
        fn f(_: &mut i32) {}
        fn g() {
            f(123);
        }
    )
}


