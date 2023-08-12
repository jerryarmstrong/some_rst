tests/ui/recursion_limit/no-value.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the parse error for no value provided to recursion_limit

#![recursion_limit]
//~^ ERROR malformed `recursion_limit` attribute input

fn main() {}


