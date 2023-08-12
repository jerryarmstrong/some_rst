tests/ui/proc-macro/append-impl.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:append-impl.rs

#![allow(warnings)]

#[macro_use]
extern crate append_impl;

trait Append {
    fn foo(&self);
}

#[derive(PartialEq,
         Append,
         Eq)]
struct A {
    inner: u32,
}

fn main() {
    A { inner: 3 }.foo();
}


