tests/ui/lint/unsafe_code/auxiliary/forge_unsafe_block.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::{Delimiter, Group, Ident, Span, TokenStream, TokenTree};

#[proc_macro]
pub fn forge_unsafe_block(input: TokenStream) -> TokenStream {
    let mut output = TokenStream::new();
    output.extend(Some(TokenTree::from(Ident::new("unsafe", Span::call_site()))));
    output.extend(Some(TokenTree::from(Group::new(Delimiter::Brace, input))));
    output
}


