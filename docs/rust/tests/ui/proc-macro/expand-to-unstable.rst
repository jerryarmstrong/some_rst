tests/ui/proc-macro/expand-to-unstable.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:derive-unstable.rs

#![allow(warnings)]

#[macro_use]
extern crate derive_unstable;

#[derive(Unstable)]
//~^ ERROR: use of unstable library feature
struct A;

fn main() {
    unsafe { foo(); }
}


