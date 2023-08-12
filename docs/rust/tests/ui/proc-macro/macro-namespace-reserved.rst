tests/ui/proc-macro/macro-namespace-reserved.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![feature(decl_macro)]
#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro]
pub fn my_macro(input: TokenStream) -> TokenStream {
    input
}

#[proc_macro_attribute]
pub fn my_macro_attr(input: TokenStream, _: TokenStream) -> TokenStream {
    input
}

#[proc_macro_derive(MyTrait)]
pub fn my_macro_derive(input: TokenStream) -> TokenStream {
    input
}

macro my_macro() {} //~ ERROR the name `my_macro` is defined multiple times
macro my_macro_attr() {} //~ ERROR the name `my_macro_attr` is defined multiple times
macro MyTrait() {} //~ ERROR the name `MyTrait` is defined multiple times

#[proc_macro_derive(SameName)]
pub fn foo(input: TokenStream) -> TokenStream {
    input
}

#[proc_macro]
pub fn SameName(input: TokenStream) -> TokenStream {
//~^ ERROR the name `SameName` is defined multiple times
    input
}


