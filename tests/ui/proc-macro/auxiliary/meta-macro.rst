tests/ui/proc-macro/auxiliary/meta-macro.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic
// edition:2018

#![feature(proc_macro_def_site)]
#![crate_type = "proc-macro"]

extern crate proc_macro;
extern crate make_macro;
use proc_macro::{TokenStream, Span};

make_macro::make_it!(print_def_site);

#[proc_macro]
pub fn dummy(input: TokenStream) -> TokenStream { input }


