tests/ui/regions/regions-no-bound-in-argument-cleanup.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::marker;

pub struct Foo<T>(marker::PhantomData<T>);

impl<T> Iterator for Foo<T> {
    type Item = T;

    fn next(&mut self) -> Option<T> {
        None
    }
}

impl<T> Drop for Foo<T> {
    fn drop(&mut self) {
        self.next();
    }
}

pub fn foo<'a>(_: Foo<&'a ()>) {}

pub fn main() {}


