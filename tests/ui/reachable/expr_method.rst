tests/ui/reachable/expr_method.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
#![allow(unused_variables)]
#![allow(unused_assignments)]
#![allow(dead_code)]
#![deny(unreachable_code)]

struct Foo;

impl Foo {
    fn foo(&self, x: !, y: usize) { }
    fn bar(&self, x: !) { }
}

fn a() {
    // the `22` is unreachable:
    Foo.foo(return, 22); //~ ERROR unreachable
}

fn b() {
    // the call is unreachable:
    Foo.bar(return); //~ ERROR unreachable
}

fn main() { }


