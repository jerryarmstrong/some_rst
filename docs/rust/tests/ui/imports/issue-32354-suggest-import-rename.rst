tests/ui/imports/issue-32354-suggest-import-rename.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused_imports)]

pub mod extension1 {
    pub trait ConstructorExtension {}
}

pub mod extension2 {
    pub trait ConstructorExtension {}
}

use extension1::ConstructorExtension;
use extension2::ConstructorExtension; //~ ERROR is defined multiple times

fn main() {}


