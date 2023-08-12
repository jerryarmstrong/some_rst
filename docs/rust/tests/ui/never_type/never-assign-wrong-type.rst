tests/ui/never_type/never-assign-wrong-type.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can't use another type in place of !

#![feature(never_type)]
#![deny(warnings)]

fn main() {
    let x: ! = "hello"; //~ ERROR mismatched types
}


