tests/ui/rust-2018/async-ident-allowed.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2015

#![deny(rust_2018_compatibility)]

// Don't make a suggestion for a raw identifier replacement unless raw
// identifiers are enabled.

fn main() {
    let async = 3; //~ ERROR: is a keyword
    //~^ WARN this is accepted in the current edition
}


