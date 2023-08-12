tests/ui/variance/variance-regions-unused-direct.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that disallow lifetime parameters that are unused.

use std::marker;

struct Bivariant<'a>; //~ ERROR parameter `'a` is never used

struct Struct<'a, 'd> { //~ ERROR parameter `'d` is never used
    field: &'a [i32]
}

trait Trait<'a, 'd> { // OK on traits
    fn method(&'a self);
}

fn main() {}


