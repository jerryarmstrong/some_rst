tests/ui/regions/regions-bound-lists-feature-gate-2.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(stable_features)]

#![feature(issue_5723_bootstrap)]

trait Foo {
    fn dummy(&self) { }
}

fn foo<'a, 'b, 'c:'a+'b, 'd>() {
}

pub fn main() { }


