tests/ui/proc-macro/quote-debug.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// force-host
// no-prefer-dynamic
// compile-flags: -Z unpretty=expanded
//
// This file is not actually used as a proc-macro - instead,
// it's just used to show the output of the `quote!` macro

#![feature(proc_macro_quote)]
#![crate_type = "proc-macro"]

extern crate proc_macro;

fn main() {
    proc_macro::quote! {
        let hello = "world";
    }
}


