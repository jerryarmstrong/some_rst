tests/ui/typeck/project-cache-issue-37154.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// Regression test for #37154: the problem here was that the cache
// results in a false error because it was caching placeholder results
// even after those placeholder regions had been popped.

trait Foo {
    fn method(&self) {}
}

struct Wrapper<T>(T);

impl<T> Foo for Wrapper<T> where for<'a> &'a T: IntoIterator<Item=&'a ()> {}

fn f(x: Wrapper<Vec<()>>) {
    x.method(); // This works.
    x.method(); // error: no method named `method`
}

fn main() { }


