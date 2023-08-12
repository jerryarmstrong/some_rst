tests/ui/issues/auxiliary/issue-8401.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // for this issue, this code must be built in a library

use std::mem;

trait A {
    fn dummy(&self) { }
}
struct B;
impl A for B {}

fn bar<T>(_: &mut A, _: &T) {}

fn foo<T>(t: &T) {
    let mut b = B;
    bar(&mut b as &mut A, t)
}


