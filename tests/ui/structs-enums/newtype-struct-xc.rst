tests/ui/structs-enums/newtype-struct-xc.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:newtype_struct_xc.rs

// pretty-expanded FIXME #23616

extern crate newtype_struct_xc;

pub fn main() {
    let _ = newtype_struct_xc::Au(2);
}


