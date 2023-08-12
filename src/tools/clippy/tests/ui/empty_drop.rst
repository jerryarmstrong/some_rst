src/tools/clippy/tests/ui/empty_drop.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::empty_drop)]
#![allow(unused)]

// should cause an error
struct Foo;

impl Drop for Foo {
    fn drop(&mut self) {}
}

// shouldn't cause an error
struct Bar;

impl Drop for Bar {
    fn drop(&mut self) {
        println!("dropping bar!");
    }
}

// should error
struct Baz;

impl Drop for Baz {
    fn drop(&mut self) {
        {}
    }
}

fn main() {}


