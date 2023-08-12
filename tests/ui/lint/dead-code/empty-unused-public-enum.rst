tests/ui/lint/dead-code/empty-unused-public-enum.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![deny(unused)]

pub enum E {}

fn main() {}


