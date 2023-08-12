tests/ui/structs-enums/struct_variant_xc.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:struct_variant_xc_aux.rs
// pretty-expanded FIXME #23616

extern crate struct_variant_xc_aux;

use struct_variant_xc_aux::Enum::StructVariant;

pub fn main() {
    let _ = StructVariant { arg: 1 };
}


