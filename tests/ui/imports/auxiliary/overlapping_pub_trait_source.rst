tests/ui/imports/auxiliary/overlapping_pub_trait_source.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /* This crate declares an item as both `prelude::*` and `m::Tr`.
 * The compiler should always suggest `m::Tr`. */

pub struct S;

pub mod prelude {
    pub use crate::m::Tr as _;
}

pub mod m {
    pub trait Tr { fn method(&self); }
    impl Tr for crate::S { fn method(&self) {} }
}


