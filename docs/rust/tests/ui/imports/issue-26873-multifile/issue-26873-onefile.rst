tests/ui/imports/issue-26873-multifile/issue-26873-onefile.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(non_snake_case)]

mod A {
    pub mod B {
        use super::*;

        pub struct S;
    }

    pub mod C {
        use super::*;
        use super::B::S;

        pub struct T;
    }

    pub use self::C::T;
}

use A::*;

fn main() {}


