tests/ui/structs-enums/enum-nullable-const-null-with-fields.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::result::Result;
use std::result::Result::Ok;

static C: Result<(), Box<isize>> = Ok(());

// This is because of yet another bad assertion (ICE) about the null side of a nullable enum.
// So we won't actually compile if the bug is present, but we check the value in main anyway.

pub fn main() {
    assert!(C.is_ok());
}


