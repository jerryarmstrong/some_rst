tests/ui/rust-2018/try-ident.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// check-pass

#![warn(rust_2018_compatibility)]

fn main() {
    try();
    //~^ WARNING `try` is a keyword in the 2018 edition
    //~| WARNING this is accepted in the current edition
}

fn try() {
    //~^ WARNING `try` is a keyword in the 2018 edition
    //~| WARNING this is accepted in the current edition
}


