tests/ui/hygiene/auxiliary/opaque-hygiene.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![feature(proc_macro_quote)]
#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::{TokenStream, quote};

#[proc_macro]
pub fn make_it(input: TokenStream) -> TokenStream {
    // `quote!` applies def-site hygiene
    quote! {
        trait Foo {
            fn my_fn(&self) {}
        }

        impl<T> Foo for T {}
        "a".my_fn();
    }
}


