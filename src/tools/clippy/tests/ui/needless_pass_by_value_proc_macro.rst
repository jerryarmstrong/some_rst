src/tools/clippy/tests/ui/needless_pass_by_value_proc_macro.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "proc-macro"]
#![warn(clippy::needless_pass_by_value)]

extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(Foo)]
pub fn foo(_input: TokenStream) -> TokenStream {
    unimplemented!()
}

#[proc_macro]
pub fn bar(_input: TokenStream) -> TokenStream {
    unimplemented!()
}

#[proc_macro_attribute]
pub fn baz(_args: TokenStream, _input: TokenStream) -> TokenStream {
    unimplemented!()
}


