tests/ui/proc-macro/derive-bad.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:derive-bad.rs

#[macro_use]
extern crate derive_bad;

#[derive(A)]
//~^ ERROR proc-macro derive produced unparseable tokens
//~| ERROR expected `:`, found `}`
struct A; //~ ERROR the name `A` is defined multiple times

fn main() {}


