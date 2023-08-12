tests/ui/structs-enums/struct_variant_xc_match.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:struct_variant_xc_aux.rs

extern crate struct_variant_xc_aux;

use struct_variant_xc_aux::Enum::{StructVariant, Variant};

pub fn main() {
    let arg = match (StructVariant { arg: 42 }) {
        Variant(_) => unreachable!(),
        StructVariant { arg } => arg
    };
    assert_eq!(arg, 42);
}


