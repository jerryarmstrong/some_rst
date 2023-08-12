tests/ui/macros/missing-bang-in-decl.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused_macros)]

macro_rules foo {
    //~^ ERROR expected `!` after `macro_rules`
    () => {};
}

macro_rules bar! {
    //~^ ERROR expected `!` after `macro_rules`
    //~^^ ERROR macro names aren't followed by a `!`
    () => {};
}

fn main() {}


