tests/incremental/issue-85197-invalid-span/auxiliary/respan.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::TokenStream;


/// Copies the resolution information (the `SyntaxContext`) of the first
/// token to all other tokens in the stream. Does not recurse into groups.
#[proc_macro]
pub fn respan(input: TokenStream) -> TokenStream {
    let first_span = input.clone().into_iter().next().unwrap().span();
    input.into_iter().map(|mut tree| {
        tree.set_span(tree.span().resolved_at(first_span));
        tree
    }).collect()
}


