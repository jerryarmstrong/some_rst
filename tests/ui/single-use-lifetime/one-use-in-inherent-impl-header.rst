tests/ui/single-use-lifetime/one-use-in-inherent-impl-header.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(single_use_lifetimes)]
#![allow(dead_code)]
#![allow(unused_variables)]

// Test that we DO warn for a lifetime used only once in an impl, and that we
// don't warn for the anonymous lifetime.

struct Foo<'f> {
    data: &'f u32
}

impl<'f> Foo<'f> { //~ ERROR `'f` only used once
    fn inherent_a(&self) {
    }
}

impl Foo<'_> {
    fn inherent_b(&self) {}
}


fn main() { }


