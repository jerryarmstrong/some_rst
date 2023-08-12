tests/ui/editions/edition-extern-crate-allowed.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:edition-extern-crate-allowed.rs
// edition:2015
// check-pass

#![warn(rust_2018_idioms)]

extern crate edition_extern_crate_allowed;
//~^ WARNING unused extern crate

fn main() {}


