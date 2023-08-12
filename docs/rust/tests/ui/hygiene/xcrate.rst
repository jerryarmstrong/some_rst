tests/ui/hygiene/xcrate.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty pretty-printing is unhygienic

// aux-build:xcrate.rs

#![feature(decl_macro)]

extern crate xcrate;

fn main() {
    xcrate::test!();
}


