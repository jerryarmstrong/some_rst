tests/ui/reachable/expr_call.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
#![allow(unused_variables)]
#![allow(unused_assignments)]
#![allow(dead_code)]
#![deny(unreachable_code)]

fn foo(x: !, y: usize) { }

fn bar(x: !) { }

fn a() {
    // the `22` is unreachable:
    foo(return, 22); //~ ERROR unreachable
}

fn b() {
    // the call is unreachable:
    bar(return); //~ ERROR unreachable
}

fn main() { }


