tests/ui/parser/virtual-structs.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test diagnostics for the removed struct inheritance feature.

virtual struct SuperStruct {
//~^ ERROR expected item, found reserved keyword `virtual`
    f1: isize,
}

struct Struct : SuperStruct;

pub fn main() {}


