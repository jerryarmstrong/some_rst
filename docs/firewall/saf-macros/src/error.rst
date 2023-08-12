saf-macros/src/error.rs
=======================

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, Data, DeriveInput, Fields};

pub const OFFSET: u32 = 777;

pub fn derive_error(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    let data = input.data;
    let variants = match data {
        Data::Enum(ref data_enum) => &data_enum.variants,
        _ => panic!(
            "`ProgramError` can be applied only to enums, {} is neither",
            name.to_string()
        ),
    };
    let off = quote! { #OFFSET };
    let variants: Vec<_> = variants
        .iter()
        .enumerate()
        .map(|(i, variant)| {
            let i = i as u32;
            let ident = &variant.ident;
            match variant.fields {
                Fields::Unit => quote!(#name::#ident => #i + #off as u32),
                Fields::Unnamed(..) => quote!(#name::#ident(..) => #i + #off as u32),
                _ => {
                    panic!("`ProgramError` can be applied only to unitary enums, {}::{} is either struct or tuple", name, ident)
                }
            }

        })
        .collect();
    let match_expr = if variants.is_empty() {
        quote! {
            match *self {}
        }
    } else {
        quote! {
            match *self {
                #(#variants,)*
            }
        }
    };

    let add_method = quote! {
        impl #name {
            #[inline]
            #[allow(trivial_numeric_casts)]
            fn to_u32(&self) -> u32 {
                #match_expr
            }
        }
    };

    let exp = quote! {

        #add_method

        use solana_program::program_error::ProgramError;
        impl Into<ProgramError> for #name {
            fn into(self) -> ProgramError {
                ProgramError::Custom(self.to_u32() as u32)
            }
        }
    };
    exp.into()
}


