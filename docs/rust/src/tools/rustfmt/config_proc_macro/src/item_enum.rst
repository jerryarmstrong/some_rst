src/tools/rustfmt/config_proc_macro/src/item_enum.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use proc_macro2::TokenStream;
use quote::quote;

use crate::attrs::*;
use crate::utils::*;

type Variants = syn::punctuated::Punctuated<syn::Variant, syn::Token![,]>;

/// Defines and implements `config_type` enum.
pub fn define_config_type_on_enum(em: &syn::ItemEnum) -> syn::Result<TokenStream> {
    let syn::ItemEnum {
        vis,
        enum_token,
        ident,
        generics,
        variants,
        ..
    } = em;

    let mod_name_str = format!("__define_config_type_on_enum_{}", ident);
    let mod_name = syn::Ident::new(&mod_name_str, ident.span());
    let variants = fold_quote(variants.iter().map(process_variant), |meta| quote!(#meta,));

    let impl_doc_hint = impl_doc_hint(&em.ident, &em.variants);
    let impl_from_str = impl_from_str(&em.ident, &em.variants);
    let impl_display = impl_display(&em.ident, &em.variants);
    let impl_serde = impl_serde(&em.ident, &em.variants);
    let impl_deserialize = impl_deserialize(&em.ident, &em.variants);

    Ok(quote! {
        #[allow(non_snake_case)]
        mod #mod_name {
            #[derive(Debug, Copy, Clone, Eq, PartialEq)]
            pub #enum_token #ident #generics { #variants }
            #impl_display
            #impl_doc_hint
            #impl_from_str
            #impl_serde
            #impl_deserialize
        }
        #vis use #mod_name::#ident;
    })
}

/// Remove attributes specific to `config_proc_macro` from enum variant fields.
fn process_variant(variant: &syn::Variant) -> TokenStream {
    let metas = variant
        .attrs
        .iter()
        .filter(|attr| !is_doc_hint(attr) && !is_config_value(attr));
    let attrs = fold_quote(metas, |meta| quote!(#meta));
    let syn::Variant { ident, fields, .. } = variant;
    quote!(#attrs #ident #fields)
}

fn impl_doc_hint(ident: &syn::Ident, variants: &Variants) -> TokenStream {
    let doc_hint = variants
        .iter()
        .map(doc_hint_of_variant)
        .collect::<Vec<_>>()
        .join("|");
    let doc_hint = format!("[{}]", doc_hint);
    quote! {
        use crate::config::ConfigType;
        impl ConfigType for #ident {
            fn doc_hint() -> String {
                #doc_hint.to_owned()
            }
        }
    }
}

fn impl_display(ident: &syn::Ident, variants: &Variants) -> TokenStream {
    let vs = variants
        .iter()
        .filter(|v| is_unit(v))
        .map(|v| (config_value_of_variant(v), &v.ident));
    let match_patterns = fold_quote(vs, |(s, v)| {
        quote! {
            #ident::#v => write!(f, "{}", #s),
        }
    });
    quote! {
        use std::fmt;
        impl fmt::Display for #ident {
            fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
                match self {
                    #match_patterns
                    _ => unimplemented!(),
                }
            }
        }
    }
}

fn impl_from_str(ident: &syn::Ident, variants: &Variants) -> TokenStream {
    let vs = variants
        .iter()
        .filter(|v| is_unit(v))
        .map(|v| (config_value_of_variant(v), &v.ident));
    let if_patterns = fold_quote(vs, |(s, v)| {
        quote! {
            if #s.eq_ignore_ascii_case(s) {
                return Ok(#ident::#v);
            }
        }
    });
    let mut err_msg = String::from("Bad variant, expected one of:");
    for v in variants.iter().filter(|v| is_unit(v)) {
        err_msg.push_str(&format!(" `{}`", v.ident));
    }

    quote! {
        impl ::std::str::FromStr for #ident {
            type Err = &'static str;

            fn from_str(s: &str) -> Result<Self, Self::Err> {
                #if_patterns
                return Err(#err_msg);
            }
        }
    }
}

fn doc_hint_of_variant(variant: &syn::Variant) -> String {
    find_doc_hint(&variant.attrs).unwrap_or(variant.ident.to_string())
}

fn config_value_of_variant(variant: &syn::Variant) -> String {
    find_config_value(&variant.attrs).unwrap_or(variant.ident.to_string())
}

fn impl_serde(ident: &syn::Ident, variants: &Variants) -> TokenStream {
    let arms = fold_quote(variants.iter(), |v| {
        let v_ident = &v.ident;
        let pattern = match v.fields {
            syn::Fields::Named(..) => quote!(#ident::v_ident{..}),
            syn::Fields::Unnamed(..) => quote!(#ident::#v_ident(..)),
            syn::Fields::Unit => quote!(#ident::#v_ident),
        };
        let option_value = config_value_of_variant(v);
        quote! {
            #pattern => serializer.serialize_str(&#option_value),
        }
    });

    quote! {
        impl ::serde::ser::Serialize for #ident {
            fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
            where
                S: ::serde::ser::Serializer,
            {
                use serde::ser::Error;
                match self {
                    #arms
                    _ => Err(S::Error::custom(format!("Cannot serialize {:?}", self))),
                }
            }
        }
    }
}

// Currently only unit variants are supported.
fn impl_deserialize(ident: &syn::Ident, variants: &Variants) -> TokenStream {
    let supported_vs = variants.iter().filter(|v| is_unit(v));
    let if_patterns = fold_quote(supported_vs, |v| {
        let config_value = config_value_of_variant(v);
        let variant_ident = &v.ident;
        quote! {
            if #config_value.eq_ignore_ascii_case(s) {
                return Ok(#ident::#variant_ident);
            }
        }
    });

    let supported_vs = variants.iter().filter(|v| is_unit(v));
    let allowed = fold_quote(supported_vs.map(config_value_of_variant), |s| quote!(#s,));

    quote! {
        impl<'de> serde::de::Deserialize<'de> for #ident {
            fn deserialize<D>(d: D) -> Result<Self, D::Error>
            where
                D: serde::Deserializer<'de>,
            {
                use serde::de::{Error, Visitor};
                use std::marker::PhantomData;
                use std::fmt;
                struct StringOnly<T>(PhantomData<T>);
                impl<'de, T> Visitor<'de> for StringOnly<T>
                where T: serde::Deserializer<'de> {
                    type Value = String;
                    fn expecting(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
                        formatter.write_str("string")
                    }
                    fn visit_str<E>(self, value: &str) -> Result<String, E> {
                        Ok(String::from(value))
                    }
                }
                let s = &d.deserialize_string(StringOnly::<D>(PhantomData))?;

                #if_patterns

                static ALLOWED: &'static[&str] = &[#allowed];
                Err(D::Error::unknown_variant(&s, ALLOWED))
            }
        }
    }
}


