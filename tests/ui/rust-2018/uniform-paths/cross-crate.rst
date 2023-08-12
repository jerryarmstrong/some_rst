tests/ui/rust-2018/uniform-paths/cross-crate.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// aux-build:cross-crate.rs

extern crate cross_crate;
use cross_crate::*;

#[built_in_attr] //~ ERROR cannot use a built-in attribute through an import
#[tool_mod::skip] //~ ERROR cannot use a tool module through an import
                  //~| ERROR cannot use a tool module through an import
fn main() {
    let _: built_in_type; // OK
}


