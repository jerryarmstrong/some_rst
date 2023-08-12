tests/ui/pattern/usefulness/unstable-gated-fields.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unstable_test_feature)]

// aux-build:unstable.rs

extern crate unstable;

use unstable::UnstableStruct;

fn main() {
    let UnstableStruct { stable, stable2, } = UnstableStruct::default();
    //~^ pattern does not mention field `unstable`

    let UnstableStruct { stable, unstable, } = UnstableStruct::default();
    //~^ pattern does not mention field `stable2`

    // OK: stable field is matched
    let UnstableStruct { stable, stable2, unstable } = UnstableStruct::default();
}


