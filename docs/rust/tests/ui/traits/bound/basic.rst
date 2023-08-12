tests/ui/traits/bound/basic.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unconditional_recursion)]

// pretty-expanded FIXME #23616

trait Foo {
}

fn b(_x: Box<dyn Foo+Send>) {
}

fn c(x: Box<dyn Foo+Sync+Send>) {
    e(x);
}

fn d(x: Box<dyn Foo+Send>) {
    e(x);
}

fn e(x: Box<dyn Foo>) {
    e(x);
}

pub fn main() { }


