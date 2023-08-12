tests/ui/never_type/cast-never.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can explicitly cast ! to another type

// check-pass

#![feature(never_type)]

fn main() {
    let x: ! = panic!();
    let y: u32 = x as u32;
}


