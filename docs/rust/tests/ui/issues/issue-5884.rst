tests/ui/issues/issue-5884.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

pub struct Foo {
    a: isize,
}

struct Bar<'a> {
    a: Box<Option<isize>>,
    b: &'a Foo,
}

fn check(a: Box<Foo>) {
    let _ic = Bar{ b: &*a, a: Box::new(None) };
}

pub fn main(){}


