tests/ui/structs-enums/auxiliary/struct_variant_xc_aux.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="struct_variant_xc_aux"]
#![crate_type = "lib"]

#[derive(Copy, Clone)]
pub enum Enum {
    Variant(u8),
    StructVariant { arg: u8 }
}


