tests/ui/regions/regions-bound-lists-feature-gate.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(stable_features)]

#![feature(issue_5723_bootstrap)]

trait Foo {
    fn dummy(&self) { }
}

fn foo<'a>(x: Box<dyn Foo + 'a>) {
}

fn bar<'a, T: 'a>() {
}

pub fn main() { }


