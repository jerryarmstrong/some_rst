tests/ui/pattern/usefulness/stable-gated-fields.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:unstable.rs

extern crate unstable;

use unstable::UnstableStruct;

fn main() {
    let UnstableStruct { stable } = UnstableStruct::default();
    //~^ pattern does not mention field `stable2` and inaccessible fields

    let UnstableStruct { stable, stable2 } = UnstableStruct::default();
    //~^ pattern requires `..` due to inaccessible fields

    // OK: stable field is matched
    let UnstableStruct { stable, stable2, .. } = UnstableStruct::default();
}


