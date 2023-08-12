tests/ui/imports/auxiliary/glob-conflict.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m1 {
    pub fn f() {}
}
mod m2 {
    pub fn f(_: u8) {}
}

pub use m1::*;
pub use m2::*;

pub mod glob {
    pub use *;
}


