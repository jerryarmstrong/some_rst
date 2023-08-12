tests/ui/type/type-mismatch-multiple.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checking that the compiler reports multiple type errors at once

fn main() { let a: bool = 1; let b: i32 = true; }
//~^ ERROR mismatched types
//~| expected `bool`, found integer
//~| ERROR mismatched types
//~| expected `i32`, found `bool`


