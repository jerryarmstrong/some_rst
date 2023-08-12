tests/ui/impl-header-lifetime-elision/explicit-and-elided-same-header.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(warnings)]

// This works for functions...
fn foo<'a>(x: &str, y: &'a str) {}

// ...so this should work for impls
impl<'a> Foo<&str> for &'a str {}
trait Foo<T> {}

fn main() {
}


