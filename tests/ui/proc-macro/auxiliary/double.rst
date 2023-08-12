tests/ui/proc-macro/auxiliary/double.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![feature(proc_macro_quote)]

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

// Outputs another copy of the struct.  Useful for testing the tokens
// seen by the proc_macro.
#[proc_macro_derive(Double)]
pub fn derive(input: TokenStream) -> TokenStream {
    quote!(mod foo { $input })
}


