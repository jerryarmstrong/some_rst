tests/ui/proc-macro/auxiliary/re-export.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro]
pub fn cause_ice(_: TokenStream) -> TokenStream {
    "
        enum IceCause {
            Variant,
        }

        pub use IceCause::Variant;
    ".parse().unwrap()
}


