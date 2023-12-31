src/tools/clippy/tests/ui/auxiliary/proc_macro_unsafe.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit=link
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::{Delimiter, Group, Ident, TokenStream, TokenTree};

#[proc_macro]
pub fn unsafe_block(input: TokenStream) -> TokenStream {
    let span = input.into_iter().next().unwrap().span();
    TokenStream::from_iter([TokenTree::Ident(Ident::new("unsafe", span)), {
        let mut group = Group::new(Delimiter::Brace, TokenStream::new());
        group.set_span(span);
        TokenTree::Group(group)
    }])
}


