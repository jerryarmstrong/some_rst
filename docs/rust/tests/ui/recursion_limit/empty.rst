tests/ui/recursion_limit/empty.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the parse error for an empty recursion_limit

#![recursion_limit = ""] //~ ERROR `limit` must be a non-negative integer
                         //~| `limit` must be a non-negative integer
                         //~| ERROR `limit` must be a non-negative integer
                         //~| `limit` must be a non-negative integer

fn main() {}


