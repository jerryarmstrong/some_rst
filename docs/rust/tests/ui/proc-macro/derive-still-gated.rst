tests/ui/proc-macro/derive-still-gated.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

#[derive_Empty] //~ ERROR cannot find attribute `derive_Empty` in this scope
struct A;

fn main() {}


