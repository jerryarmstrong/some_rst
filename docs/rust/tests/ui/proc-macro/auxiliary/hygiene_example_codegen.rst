tests/ui/proc-macro/auxiliary/hygiene_example_codegen.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![feature(proc_macro_quote)]
#![crate_type = "proc-macro"]

extern crate proc_macro as proc_macro_renamed; // This does not break `quote!`

use proc_macro_renamed::{TokenStream, quote};

#[proc_macro]
pub fn hello(input: TokenStream) -> TokenStream {
    quote!(hello_helper!($input))
    //^ `hello_helper!` always resolves to the following proc macro,
    //| no matter where `hello!` is used.
}

#[proc_macro]
pub fn hello_helper(input: TokenStream) -> TokenStream {
    quote! {
        extern crate hygiene_example; // This is never a conflict error
        let string = format!("hello {}", $input);
        //^ `format!` always resolves to the prelude macro,
        //| even if a different `format!` is in scope where `hello!` is used.
        hygiene_example::print(&string)
    }
}


