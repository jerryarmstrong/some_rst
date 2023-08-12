tests/ui/imports/issue-45829/rename-use-with-tabs.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub struct A;

    pub mod bar {
        pub struct B;
    }
}

use foo::{A, bar::B    as    A};
//~^ ERROR is defined multiple times

fn main() {}


