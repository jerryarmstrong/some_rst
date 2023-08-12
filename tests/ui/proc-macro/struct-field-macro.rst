tests/ui/proc-macro/struct-field-macro.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// aux-build:derive-nothing.rs

#[macro_use]
extern crate derive_nothing;

macro_rules! int {
    () => { i32 }
}

#[derive(Nothing)]
struct S {
    x: int!(),
}

fn main() {}


