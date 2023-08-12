compiler/rustc_mir_transform/src/coverage/test_macros/src/lib.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use proc_macro::TokenStream;

#[proc_macro]
pub fn let_bcb(item: TokenStream) -> TokenStream {
    format!("let bcb{} = graph::BasicCoverageBlock::from_usize({});", item, item).parse().unwrap()
}


