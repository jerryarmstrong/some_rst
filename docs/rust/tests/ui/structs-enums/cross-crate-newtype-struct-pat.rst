tests/ui/structs-enums/cross-crate-newtype-struct-pat.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:newtype_struct_xc.rs


extern crate newtype_struct_xc;

pub fn main() {
    let x = newtype_struct_xc::Au(21);
    match x {
        newtype_struct_xc::Au(n) => assert_eq!(n, 21)
    }
}


