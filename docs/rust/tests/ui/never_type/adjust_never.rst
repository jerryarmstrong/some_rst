tests/ui/never_type/adjust_never.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a variable of type ! can coerce to another type.

// check-pass

#![feature(never_type)]

fn main() {
    let x: ! = panic!();
    let y: u32 = x;
}


