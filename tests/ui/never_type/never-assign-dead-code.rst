tests/ui/never_type/never-assign-dead-code.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that an assignment of type ! makes the rest of the block dead code.

// check-pass

#![feature(never_type)]
#![warn(unused)]

fn main() {
    let x: ! = panic!("aah"); //~ WARN unused
    drop(x); //~ WARN unreachable
    //~^ WARN unreachable
}


