tests/ui/imports/issue-45829/rename-use-vs-extern.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:issue-45829-b.rs

extern crate issue_45829_b;
use std as issue_45829_b;
//~^ ERROR is defined multiple times

fn main() {}


