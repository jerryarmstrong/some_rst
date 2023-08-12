tests/ui/rust-2018/edition-lint-nested-empty-paths.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![feature(rust_2018_preview)]
#![deny(absolute_paths_not_starting_with_crate)]
#![allow(unused_imports)]
#![allow(dead_code)]

pub(crate) mod foo {
    pub(crate) mod bar {
        pub(crate) mod baz { }
        pub(crate) mod baz1 { }

        pub(crate) struct XX;
    }
}

use foo::{bar::{baz::{}}};
//~^ ERROR absolute paths must start with
//~| WARN this is accepted in the current edition

use foo::{bar::{XX, baz::{}}};
//~^ ERROR absolute paths must start with
//~| WARN this is accepted in the current edition
//~| ERROR absolute paths must start with
//~| WARN this is accepted in the current edition

use foo::{bar::{baz::{}, baz1::{}}};
//~^ ERROR absolute paths must start with
//~| WARN this is accepted in the current edition
//~| ERROR absolute paths must start with
//~| WARN this is accepted in the current edition

fn main() {
}


