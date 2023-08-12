tests/ui/proc-macro/empty-crate.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports)]
// aux-build:empty-crate.rs

#[macro_use]
extern crate empty_crate;

fn main() {}


