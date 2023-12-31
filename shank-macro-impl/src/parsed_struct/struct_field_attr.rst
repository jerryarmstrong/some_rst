shank-macro-impl/src/parsed_struct/struct_field_attr.rs
=======================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    use std::collections::HashSet;

use syn::Attribute;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StructFieldAttr {
    Padding,
}

impl From<&StructFieldAttr> for String {
    fn from(attr: &StructFieldAttr) -> Self {
        match attr {
            StructFieldAttr::Padding => "padding".to_string(),
        }
    }
}

pub struct StructFieldAttrs(pub HashSet<StructFieldAttr>);

impl From<&[Attribute]> for StructFieldAttrs {
    fn from(attrs: &[Attribute]) -> Self {
        Self(
            attrs
                .iter()
                .filter_map(|attr| {
                    if attr.path.is_ident("padding") {
                        Some(StructFieldAttr::Padding)
                    } else {
                        None
                    }
                })
                .collect(),
        )
    }
}


