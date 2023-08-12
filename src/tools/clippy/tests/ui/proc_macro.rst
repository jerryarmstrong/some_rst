src/tools/clippy/tests/ui/proc_macro.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Check that we correctly lint procedural macros.
#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

#[allow(dead_code)]
fn f() {
    let _x = 3.14;
}

#[proc_macro]
pub fn mybangmacro(t: TokenStream) -> TokenStream {
    t
}

#[proc_macro_derive(MyDerivedTrait)]
pub fn myderive(t: TokenStream) -> TokenStream {
    t
}

#[proc_macro_attribute]
pub fn myattribute(t: TokenStream, a: TokenStream) -> TokenStream {
    t
}


