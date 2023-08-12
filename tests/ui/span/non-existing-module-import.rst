tests/ui/span/non-existing-module-import.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::bar::{foo1, foo2}; //~ ERROR unresolved import

fn main() {}


