tests/ui/codemap_tests/overlapping_inherent_impls.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that you cannot define items with the same name in overlapping inherent
// impl blocks.

#![allow(unused)]

struct Foo;

impl Foo {
    fn id() {} //~ ERROR duplicate definitions
}

impl Foo {
    fn id() {}
}

struct Bar<T>(T);

impl<T> Bar<T> {
    fn bar(&self) {} //~ ERROR duplicate definitions
}

impl Bar<u32> {
    fn bar(&self) {}
}

struct Baz<T>(T);

impl<T: Copy> Baz<T> {
    fn baz(&self) {} //~ ERROR duplicate definitions
}

impl<T> Baz<Vec<T>> {
    fn baz(&self) {}
}

fn main() {}


