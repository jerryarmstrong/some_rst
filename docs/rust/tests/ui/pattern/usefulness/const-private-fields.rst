tests/ui/pattern/usefulness/const-private-fields.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
//
// Check that we don't ignore private fields in usefulness checking
#![deny(unreachable_patterns)]

mod inner {
    #[derive(PartialEq, Eq)]
    pub struct PrivateField {
        pub x: bool,
        y: bool,
    }

    pub const FOO: PrivateField = PrivateField { x: true, y: true };
    pub const BAR: PrivateField = PrivateField { x: true, y: false };
}
use inner::*;

fn main() {
    match FOO {
        FOO => {}
        BAR => {}
        _ => {}
    }

    match FOO {
        FOO => {}
        PrivateField { x: true, .. } => {}
        _ => {}
    }
}


