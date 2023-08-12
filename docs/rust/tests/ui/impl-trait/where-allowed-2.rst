tests/ui/impl-trait/where-allowed-2.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

fn in_adt_in_return() -> Vec<impl Debug> { panic!() }
//~^ ERROR type annotations needed

fn main() {}


