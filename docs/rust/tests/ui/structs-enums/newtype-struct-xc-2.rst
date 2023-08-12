tests/ui/structs-enums/newtype-struct-xc-2.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:newtype_struct_xc.rs

// pretty-expanded FIXME #23616

extern crate newtype_struct_xc;
use newtype_struct_xc::Au;

fn f() -> Au {
    Au(2)
}

pub fn main() {
    let _ = f();
}


