tests/ui/lint/unused/lint-unused-mut-self.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused_assignments)]
#![allow(unused_variables)]
#![allow(dead_code)]
#![deny(unused_mut)]

struct Foo;
impl Foo {
    fn foo(mut self) {} //~ ERROR: variable does not need to be mutable
    fn bar(mut self: Box<Foo>) {} //~ ERROR: variable does not need to be mutable
}

fn main() {}


