src/tools/rustfmt/config_proc_macro/src/config_type.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use proc_macro2::TokenStream;

use crate::item_enum::define_config_type_on_enum;
use crate::item_struct::define_config_type_on_struct;

/// Defines `config_type` on enum or struct.
// FIXME: Implement this on struct.
pub fn define_config_type(input: &syn::Item) -> TokenStream {
    match input {
        syn::Item::Struct(st) => define_config_type_on_struct(st),
        syn::Item::Enum(en) => define_config_type_on_enum(en),
        _ => panic!("Expected enum or struct"),
    }
    .unwrap()
}


