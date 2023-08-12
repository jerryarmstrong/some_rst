tests/ui/tag-that-dare-not-speak-its-name.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #876

use std::vec::Vec;

fn last<T>(v: Vec<&T> ) -> std::option::Option<T> {
    ::std::panic!();
}

fn main() {
    let y;
    let x : char = last(y);
    //~^ ERROR mismatched types
    //~| expected type `char`
    //~| found enum `Option<_>`
    //~| expected `char`, found enum `Option`
}


