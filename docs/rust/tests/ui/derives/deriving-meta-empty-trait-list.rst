tests/ui/derives/deriving-meta-empty-trait-list.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(unused)]

#[derive()] // OK
struct _Bar;

pub fn main() {}


