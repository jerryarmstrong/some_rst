tests/ui/single-use-lifetime/zero-uses-in-impl.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we DO warn when lifetime name is not used at all.

#![deny(unused_lifetimes)]
#![allow(dead_code, unused_variables)]

struct Foo {}

impl<'a> Foo {} //~ ERROR `'a` never used

fn main() {}


