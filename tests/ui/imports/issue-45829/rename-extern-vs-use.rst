tests/ui/imports/issue-45829/rename-extern-vs-use.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:issue-45829-b.rs

mod foo {
    pub mod bar {}
}

use foo::bar;
extern crate issue_45829_b as bar;
//~^ ERROR the name `bar` is defined multiple times

fn main() {}


