tests/ui/rfc-2008-non-exhaustive/enum-as-cast.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:enums.rs

extern crate enums;

use enums::FieldLessWithNonExhaustiveVariant;

fn main() {
    let e = FieldLessWithNonExhaustiveVariant::default();
    let d = e as u8; //~ ERROR casting `FieldLessWithNonExhaustiveVariant` as `u8` is invalid [E0606]
    assert_eq!(d, 0);
}


