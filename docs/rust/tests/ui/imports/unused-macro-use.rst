tests/ui/imports/unused-macro-use.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused)]

#[macro_use] //~ ERROR unused `#[macro_use]` import
extern crate core;

#[macro_use(
    panic //~ ERROR unused `#[macro_use]` import
)]
extern crate core as core_2;

fn main() {}


