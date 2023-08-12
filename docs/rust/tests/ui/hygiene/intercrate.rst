tests/ui/hygiene/intercrate.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-pretty pretty-printing is unhygienic

// aux-build:intercrate.rs

#![feature(decl_macro)]

extern crate intercrate;

fn main() {
    assert_eq!(intercrate::foo::m!(), 1);
    //~^ ERROR type `fn() -> u32 {foo::bar::f}` is private
}


