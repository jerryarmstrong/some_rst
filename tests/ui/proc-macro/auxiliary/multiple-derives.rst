tests/ui/proc-macro/auxiliary/multiple-derives.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

macro_rules! make_derives {
    ($($name:ident),*) => {
        $(
            #[proc_macro_derive($name)]
            pub fn $name(input: TokenStream) -> TokenStream {
                println!("Derive {}: {}", stringify!($name), input);
                TokenStream::new()
            }
        )*
    }
}

make_derives!(First, Second, Third, Fourth, Fifth);


