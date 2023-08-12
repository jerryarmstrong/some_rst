shank-render/src/consts.rs
==========================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    use proc_macro2::TokenStream;
use quote::quote;

pub fn solana_program_pubkey() -> TokenStream {
    quote! { ::solana_program::pubkey::Pubkey }
}


