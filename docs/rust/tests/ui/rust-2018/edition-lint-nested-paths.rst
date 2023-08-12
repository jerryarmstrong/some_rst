tests/ui/rust-2018/edition-lint-nested-paths.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![feature(rust_2018_preview)]
#![deny(absolute_paths_not_starting_with_crate)]

use foo::{a, b};
//~^ ERROR absolute paths must start with
//~| this is accepted in the current edition
//~| ERROR absolute paths must start with
//~| this is accepted in the current edition

mod foo {
    pub(crate) fn a() {}
    pub(crate) fn b() {}
    pub(crate) fn c() {}
}

fn main() {
    a();
    b();

    {
        use foo::{self as x, c};
        //~^ ERROR absolute paths must start with
        //~| this is accepted in the current edition
        //~| ERROR absolute paths must start with
        //~| this is accepted in the current edition
        x::a();
        c();
    }
}


