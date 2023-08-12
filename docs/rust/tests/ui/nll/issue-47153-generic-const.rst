tests/ui/nll/issue-47153-generic-const.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Regression test for #47153: constants in a generic context (such as
// a trait) used to ICE.

#![allow(warnings)]

trait Foo {
    const B: bool = true;
}

struct Bar<T> { x: T }

impl<T> Bar<T> {
    const B: bool = true;
}

fn main() { }


