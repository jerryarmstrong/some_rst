tests/ui/associated-inherent-types/assoc-inherent-private.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(inherent_associated_types)]
#![allow(incomplete_features)]

mod m {
    pub struct T;
    impl T {
        type P = ();
    }
}
type U = m::T::P; //~ ERROR associated type `P` is private

mod n {
    pub mod n {
        pub struct T;
        impl T {
            pub(super) type P = bool;
        }
    }
    type U = n::T::P;
}
type V = n::n::T::P; //~ ERROR associated type `P` is private

fn main() {}


