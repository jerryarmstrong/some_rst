tests/ui/imports/unused-import-issue-87973.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![deny(unused_imports)]

// Check that attributes get removed too. See #87973.
#[deprecated]
#[allow(unsafe_code)]
#[cfg(not(foo))]
use std::fs;
//~^ ERROR unused import

fn main() {}


