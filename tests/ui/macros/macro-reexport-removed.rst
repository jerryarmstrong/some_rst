tests/ui/macros/macro-reexport-removed.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:two_macros.rs

#![feature(macro_reexport)] //~ ERROR feature has been removed

#[macro_reexport(macro_one)] //~ ERROR cannot find attribute `macro_reexport` in this scope
extern crate two_macros;

fn main() {}


