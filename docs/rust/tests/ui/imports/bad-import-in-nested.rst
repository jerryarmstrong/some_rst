tests/ui/imports/bad-import-in-nested.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition: 2021

#![allow(unused)]

mod A {
    pub(crate) type AA = ();
    pub(crate) type BB = ();

    mod A2 {
        use super::{super::C::D::AA, AA as _};
        //~^ ERROR unresolved import
    }
}

mod C {
    pub mod D {}
}

mod B {
    use crate::C::{self, AA};
    //~^ ERROR unresolved import

    use crate::{A, C::BB};
    //~^ ERROR unresolved import
}

fn main() {}


