tests/ui/trivial-bounds/trivial-bounds-inconsistent-well-formed.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that inconsistent bounds are used in well-formedness checks
#![feature(trivial_bounds)]

use std::fmt::Debug;

pub fn foo() where Vec<str>: Debug, str: Copy {
    //~^ WARNING Debug does not depend on any type or lifetime
    //~| WARNING Copy does not depend on any type or lifetime
    let x = vec![*"1"];
    println!("{:?}", x);
}

fn main() {}


