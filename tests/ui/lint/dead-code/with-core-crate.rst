tests/ui/lint/dead-code/with-core-crate.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(dead_code)]
#![allow(unreachable_code)]

#[macro_use]
extern crate core;

fn foo() { //~ ERROR function `foo` is never used

    // none of these should have any dead_code exposed to the user
    panic!();

    panic!("foo");

    panic!("bar {}", "baz")
}


fn main() {}


