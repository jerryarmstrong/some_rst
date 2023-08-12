tests/ui/span/type-binding.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #28158
// Test the type binding span doesn't include >>

use std::ops::Deref;

fn homura<T: Deref<Trget = i32>>(_: T) {}
//~^ ERROR not found

fn main() {}


